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
   2) Ajoute tes 2 secrets (Worker → Settings → Variables) :
        TIKTOK_ACCESS_TOKEN  = (TikTok Events Manager → ton pixel → Settings
                                → Generate Access Token)
        TIKTOK_PIXEL_ID      = D8S207JC77U4HL2FF3VG  (ton pixel actuel)
      (Optionnel) ALLOWED_ORIGIN = https://lumera-skincare.com
   3) Dans analytics.js, mets CONFIG.eventsApiUrl = l'URL du Worker.
      → le suivi server-side s'active automatiquement (après consentement).
   ===================================================================== */

const TIKTOK_ENDPOINT = 'https://business-api.tiktok.com/open_api/v1.3/event/track/';

async function sha256(value) {
  if (!value) return undefined;
  const data = new TextEncoder().encode(String(value).trim().toLowerCase());
  const buf = await crypto.subtle.digest('SHA-256', data);
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function cors(origin) {
  return {
    'Access-Control-Allow-Origin': origin || '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400'
  };
}

export default {
  async fetch(request, env) {
    const allowed = env.ALLOWED_ORIGIN || '*';
    if (request.method === 'OPTIONS') return new Response(null, { headers: cors(allowed) });
    if (request.method !== 'POST') return new Response('Method Not Allowed', { status: 405, headers: cors(allowed) });

    let body;
    try { body = await request.json(); } catch (e) { return new Response('Bad JSON', { status: 400, headers: cors(allowed) }); }

    // Données envoyées par le client (analytics.js)
    const { event, event_id, value, currency, content_name, url, ttclid, ttp, email } = body || {};
    if (!event) return new Response('Missing event', { status: 400, headers: cors(allowed) });

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
          value: typeof value === 'number' ? value : undefined,
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
