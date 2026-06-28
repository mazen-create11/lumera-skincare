/* =====================================================================
   LUMÉRA — TikTok Events API (suivi server-side)  •  Cloudflare Worker
   ---------------------------------------------------------------------
   POURQUOI : le pixel navigateur perd des events (bloqueurs de pub, iOS,
   refus cookies). Le suivi server-side renvoie les mêmes events depuis un
   serveur → TikTok en récupère davantage = meilleure optimisation des pubs.
   Reste soumis au consentement : le client n'appelle ce Worker qu'après
   « Accepter » (cf. analytics.js → lumeraTrack).

   ─── DÉPLOIEMENT (3 étapes, gratuit) ───────────────────────────────
   1) Crée un compte Cloudflare → Workers & Pages → Create Worker.
      Colle ce fichier, déploie. Tu obtiens une URL :
      https://lumera-events.<ton-sous-domaine>.workers.dev
   2) Ajoute tes secrets/variables (Worker → Settings → Variables) :
        TIKTOK_ACCESS_TOKEN  = (TikTok Events Manager → ton pixel → Settings
                                → Generate Access Token)
        TIKTOK_PIXEL_ID      = D8S207JC77U4HL2FF3VG  (ton pixel actuel)
        ALLOWED_ORIGIN       = OBLIGATOIRE. Liste d'origines autorisées,
                               séparées par des virgules. Sans elle, le Worker
                               refuse TOUTES les requêtes (403) — on ne relaie
                               jamais avec un fallback '*' (= proxy ouvert :
                               un tiers pourrait injecter de faux events
                               AddToCart/CompletePayment et polluer le pixel).
                               Origines de prod à mettre :
                                 https://mazen-create11.github.io
                               + le domaine custom futur, ex.
                                 https://lumera-skincare.com
                               Exemple multi-origines :
                                 https://mazen-create11.github.io,https://lumera-skincare.com
   3) Dans analytics.js, mets CONFIG.eventsApiUrl = l'URL du Worker.
      → le suivi server-side s'active automatiquement (après consentement).

   ─── DURCISSEMENT (audit sécu) ─────────────────────────────────────
   • ALLOWED_ORIGIN est REQUISE et validée contre l'en-tête Origin entrant.
   • Le payload est validé (event en liste blanche, value bornée) avant relais.
   • Recommandé EN PLUS : un rate-limit côté Cloudflare WAF (Security → WAF
     → Rate limiting rules) sur la route du Worker, pour brider les abus
     d'un client autorisé (ex. 60 req/min par IP).
   ===================================================================== */

const TIKTOK_ENDPOINT = 'https://business-api.tiktok.com/open_api/v1.3/event/track/';

// Events TikTok autorisés au relais (alignés sur analytics.js / pixel TikTok).
const ALLOWED_EVENTS = new Set([
  'PageView', 'ViewContent', 'AddToCart', 'InitiateCheckout',
  'CompletePayment', 'Lead', 'Subscribe', 'AddPaymentInfo',
  'PlaceAnOrder', 'CompleteRegistration', 'Search'
]);

const MAX_VALUE = 100000; // borne haute anti-injection sur le montant

// Parse ALLOWED_ORIGIN → liste nettoyée. Vide si la variable est absente.
function parseAllowedOrigins(env) {
  return String(env.ALLOWED_ORIGIN || '')
    .split(',')
    .map(o => o.trim())
    .filter(Boolean);
}

async function sha256(value) {
  if (!value) return undefined;
  const data = new TextEncoder().encode(String(value).trim().toLowerCase());
  const buf = await crypto.subtle.digest('SHA-256', data);
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

// CORS : ne reflète QUE l'origine autorisée fournie (jamais '*').
function cors(origin) {
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

export default {
  async fetch(request, env) {
    const allowList = parseAllowedOrigins(env);
    const reqOrigin = request.headers.get('Origin') || '';
    const originOk = allowList.length > 0 && allowList.includes(reqOrigin);

    // ALLOWED_ORIGIN absente/vide → on refuse tout (pas de proxy ouvert).
    if (allowList.length === 0) {
      return new Response('Forbidden: ALLOWED_ORIGIN not configured', { status: 403 });
    }
    // Origin entrant non autorisé → 403, aucun relais vers TikTok.
    if (!originOk) {
      return new Response('Forbidden: origin not allowed', { status: 403 });
    }

    // À partir d'ici, reqOrigin est une origine autorisée → on peut la refléter.
    const allowed = reqOrigin;

    if (request.method === 'OPTIONS') return new Response(null, { headers: cors(allowed) });
    if (request.method !== 'POST') return new Response('Method Not Allowed', { status: 405, headers: cors(allowed) });

    let body;
    try { body = await request.json(); } catch (e) { return new Response('Bad JSON', { status: 400, headers: cors(allowed) }); }

    // Données envoyées par le client (analytics.js)
    const { event, event_id, value, currency, content_name, url, ttclid, ttp, email } = body || {};

    // Validation stricte du payload avant tout relais.
    if (!event || !ALLOWED_EVENTS.has(event)) {
      return new Response('Invalid event', { status: 400, headers: cors(allowed) });
    }
    // value optionnelle, mais si fournie : nombre fini, >= 0 et <= MAX_VALUE.
    let safeValue;
    if (value !== undefined && value !== null) {
      if (typeof value !== 'number' || !Number.isFinite(value) || value < 0 || value > MAX_VALUE) {
        return new Response('Invalid value', { status: 400, headers: cors(allowed) });
      }
      safeValue = value;
    }

    const payload = {
      event_source: 'web',
      event_source_id: env.TIKTOK_PIXEL_ID,
      data: [{
        event,
        event_time: Math.floor(Date.now() / 1000),
        event_id: event_id || crypto.randomUUID(),
        user: {
          ttclid: ttclid || undefined,
          ttp: ttp || undefined,
          email: await sha256(email),
          ip: request.headers.get('CF-Connecting-IP') || undefined,
          user_agent: request.headers.get('User-Agent') || undefined
        },
        page: { url: url || undefined },
        properties: {
          currency: currency || 'EUR',
          value: safeValue,
          contents: content_name ? [{ content_name }] : undefined
        }
      }]
    };

    try {
      const tt = await fetch(TIKTOK_ENDPOINT, {
        method: 'POST',
        headers: { 'Access-Token': env.TIKTOK_ACCESS_TOKEN, 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const out = await tt.text();
      return new Response(out, { status: tt.status, headers: { ...cors(allowed), 'Content-Type': 'application/json' } });
    } catch (e) {
      return new Response(JSON.stringify({ error: String(e) }), { status: 502, headers: { ...cors(allowed), 'Content-Type': 'application/json' } });
    }
  }
};
