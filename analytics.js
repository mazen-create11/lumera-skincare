/* =====================================================================
   LUMÉRA — Tracking (GA4 + Meta Pixel + TikTok Pixel)
   ---------------------------------------------------------------------
   👉 REMPLACE les 3 ID ci-dessous par les tiens, puis c'est tout :
      - GA4    : crée une propriété sur analytics.google.com → "G-XXXXXXXXXX"
      - Meta   : Gestionnaire d'événements Meta → ID du pixel (chiffres)
      - TikTok : TikTok Ads Manager → Événements → Web → ID du pixel
   Tant qu'un ID contient des "X", il n'est PAS chargé (aucune erreur).
   Les événements (add_to_cart, checkout) sont déjà câblés via cart.js.
   ===================================================================== */
(function () {
  var CONFIG = {
    ga4:    'G-XXXXXXXXXX',          // Google Analytics 4
    meta:   'XXXXXXXXXXXXXXX',       // Meta (Facebook/Instagram) Pixel
    tiktok: 'XXXXXXXXXXXXXXXXXXXX'   // TikTok Pixel
  };
  function isSet(v) { return v && v.indexOf('X') === -1; }

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

  /* ---- API unifiée : appelée par cart.js ---- */
  window.lumeraTrack = function (event, data) {
    data = data || {};
    try {
      if (window.gtag) gtag('event', event, { value: data.value, currency: 'EUR', items: data.name ? [{ item_name: data.name }] : undefined });
      if (window.fbq) {
        var m = { add_to_cart: 'AddToCart', begin_checkout: 'InitiateCheckout', view_item: 'ViewContent', purchase: 'Purchase' };
        if (m[event]) fbq('track', m[event], { value: data.value, currency: 'EUR', content_name: data.name });
      }
      if (window.ttq) {
        var t = { add_to_cart: 'AddToCart', begin_checkout: 'InitiateCheckout', view_item: 'ViewContent', purchase: 'CompletePayment' };
        if (t[event]) ttq.track(t[event], { value: data.value, currency: 'EUR', content_name: data.name });
      }
    } catch (e) {}
  };
})();
