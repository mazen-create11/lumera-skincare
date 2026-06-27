/* =====================================================================
   LUMÉRA — Tracking (GA4 + Meta Pixel + TikTok Pixel)
   ---------------------------------------------------------------------
   👉 REMPLACE les 3 ID ci-dessous par les tiens, puis c'est tout :
      - GA4    : crée une propriété sur analytics.google.com → "G-XXXXXXXXXX"
      - Meta   : Gestionnaire d'événements Meta → ID du pixel (chiffres)
      - TikTok : TikTok Ads Manager → Événements → Web → ID du pixel
   Tant qu'un ID contient des "X", il n'est PAS chargé (aucune erreur).
   Les événements (add_to_cart, checkout) sont déjà câblés via cart.js.

   ⚖️  RGPD : les pixels ne se chargent QU'APRÈS consentement (consent.js).
   lumeraInitTracking() est appelée par la bannière quand l'utilisateur
   accepte. Aucun cookie tiers n'est posé avant ce clic.
   ===================================================================== */
(function () {
  var CONFIG = {
    ga4:    'G-XXXXXXXXXX',          // Google Analytics 4
    meta:   'XXXXXXXXXXXXXXX',       // Meta (Facebook/Instagram) Pixel
    tiktok: 'D8S207JC77U4HL2FF3VG',  // TikTok Pixel
    // Suivi server-side (TikTok Events API) — colle ici l'URL de ton Worker
    // Cloudflare (cf. events-api-worker.js). Vide = désactivé, rien ne change.
    eventsApiUrl: ''
  };
  function isSet(v) { return v && v.indexOf('X') === -1; }

  // Identifiants de clic TikTok (pour rattacher l'event à la pub) + dédup
  function cookie(n) { var m = document.cookie.match('(^|;)\\s*' + n + '\\s*=\\s*([^;]+)'); return m ? m.pop() : undefined; }
  function ttclid() { try { return new URLSearchParams(location.search).get('ttclid') || cookie('ttclid') || undefined; } catch (e) { return undefined; } }
  function newEventId() { return 'lm_' + Date.now() + '_' + Math.floor(Math.random() * 1e6).toString(36); }

  /* ---- Chargé uniquement sur consentement (cf. consent.js) ---- */
  window.lumeraInitTracking = function () {
    if (window.__lumeraTracking) return;        // une seule fois
    window.__lumeraTracking = true;

    /* ---- Google Analytics 4 ---- */
    if (isSet(CONFIG.ga4)) {
      var g = document.createElement('script');
      g.async = true; g.src = 'https://www.googletagmanager.com/gtag/js?id=' + CONFIG.ga4;
      document.head.appendChild(g);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { dataLayer.push(arguments); };
      gtag('js', new Date());
      gtag('config', CONFIG.ga4);
    }

    /* ---- Meta Pixel ---- */
    if (isSet(CONFIG.meta)) {
      !function (f, b, e, v, n, t, s) {
        if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
        if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
        t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
      }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', CONFIG.meta);
      fbq('track', 'PageView');
    }

    /* ---- TikTok Pixel ---- */
    if (isSet(CONFIG.tiktok)) {
      !function (w, d, t) {
        w.TiktokAnalyticsObject = t; var ttq = w[t] = w[t] || [];
        ttq.methods = ['page', 'track', 'identify', 'instances', 'debug', 'on', 'off', 'once', 'ready', 'alias', 'group', 'enableCookie', 'disableCookie'];
        ttq.setAndDefer = function (e, n) { e[n] = function () { e.push([n].concat(Array.prototype.slice.call(arguments, 0))); }; };
        for (var i = 0; i < ttq.methods.length; i++) ttq.setAndDefer(ttq, ttq.methods[i]);
        ttq.instance = function (e) { for (var n = ttq._i[e] || [], i = 0; i < ttq.methods.length; i++) ttq.setAndDefer(n, ttq.methods[i]); return n; };
        ttq.load = function (e, n) {
          var r = 'https://analytics.tiktok.com/i18n/pixel/events.js'; ttq._i = ttq._i || {}; ttq._i[e] = []; ttq._i[e]._u = r;
          ttq._t = ttq._t || {}; ttq._t[e] = +new Date; ttq._o = ttq._o || {}; ttq._o[e] = n || {};
          var o = d.createElement('script'); o.type = 'text/javascript'; o.async = !0; o.src = r + '?sdkid=' + e + '&lib=' + t;
          var a = d.getElementsByTagName('script')[0]; a.parentNode.insertBefore(o, a);
        };
        ttq.load(CONFIG.tiktok); ttq.page();
      }(window, document, 'ttq');
    }
  };

  /* ---- Consentement déjà accordé lors d'une visite précédente ? ---- */
  try { if (localStorage.getItem('lumera_consent') === 'granted') window.lumeraInitTracking(); } catch (e) {}

  // Envoi server-side (TikTok Events API via Worker) — même event_id que le
  // pixel → TikTok déduplique. Ne part qu'après consentement + URL configurée.
  function sendServer(ttName, eid, data) {
    try {
      fetch(CONFIG.eventsApiUrl, {
        method: 'POST', keepalive: true,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          event: ttName, event_id: eid,
          value: typeof data.value === 'number' ? data.value : undefined,
          currency: 'EUR', content_name: data.name,
          url: location.href, ttclid: ttclid(), ttp: cookie('_ttp')
        })
      }).catch(function () {});
    } catch (e) {}
  }

  /* ---- API unifiée : appelée par cart.js (no-op tant que pixels absents) ---- */
  window.lumeraTrack = function (event, data) {
    data = data || {};
    var eid = newEventId();
    try {
      if (window.gtag) gtag('event', event, { value: data.value, currency: 'EUR', items: data.name ? [{ item_name: data.name }] : undefined });
      if (window.fbq) {
        var m = { add_to_cart: 'AddToCart', begin_checkout: 'InitiateCheckout', view_item: 'ViewContent', purchase: 'Purchase' };
        if (m[event]) fbq('track', m[event], { value: data.value, currency: 'EUR', content_name: data.name }, { eventID: eid });
      }
      var ttName = ({ add_to_cart: 'AddToCart', begin_checkout: 'InitiateCheckout', view_item: 'ViewContent', purchase: 'CompletePayment' })[event];
      if (window.ttq && ttName) ttq.track(ttName, { value: data.value, currency: 'EUR', content_name: data.name }, { event_id: eid });
      // Server-side : uniquement si consentement accordé ET Worker configuré
      if (ttName && CONFIG.eventsApiUrl && window.__lumeraTracking) sendServer(ttName, eid, data);
    } catch (e) {}
  };
})();
