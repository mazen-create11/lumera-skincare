/* =====================================================================
   LUMÉRA — Bannière de consentement cookies (RGPD / CNIL)
   ---------------------------------------------------------------------
   • Aucun cookie de mesure/pub n'est posé avant le clic « Accepter ».
   • « Accepter » et « Refuser » ont le même poids visuel (exigence CNIL).
   • Le choix est mémorisé (localStorage 'lumera_consent' = granted|denied).
   • window.lumeraOpenConsent() rouvre la bannière (lien « Cookies » footer).
   • Dépend de analytics.js (window.lumeraInitTracking) chargé avant.
   ===================================================================== */
(function () {
  var KEY = 'lumera_consent';
  function getChoice() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setChoice(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  var STYLE = [
    '#lmConsent{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;',
    'background:#FFFDFB;border-top:1px solid rgba(168,89,104,.22);',
    'box-shadow:0 -10px 40px rgba(61,26,36,.10);',
    'font-family:"Hanken Grotesk",system-ui,sans-serif;color:#3D1A24;',
    'transform:translateY(110%);transition:transform .4s cubic-bezier(.16,.84,.44,1);}',
    '#lmConsent.show{transform:translateY(0);}',
    '#lmConsent .lmc-in{max-width:1080px;margin:0 auto;padding:1.1rem 1.4rem;',
    'display:flex;align-items:center;gap:1.4rem;flex-wrap:wrap;justify-content:space-between;}',
    '#lmConsent p{margin:0;font-size:.86rem;line-height:1.55;color:#5C2D3A;flex:1 1 380px;}',
    '#lmConsent a{color:#A85968;text-decoration:underline;text-underline-offset:2px;}',
    '#lmConsent .lmc-btns{display:flex;gap:.6rem;flex:0 0 auto;}',
    '#lmConsent button{font-family:inherit;font-size:.82rem;font-weight:600;letter-spacing:.01em;',
    'padding:.62rem 1.25rem;border-radius:999px;cursor:pointer;border:1px solid #A85968;transition:all .2s;}',
    '#lmConsent .lmc-refuse{background:transparent;color:#A85968;}',
    '#lmConsent .lmc-refuse:hover{background:rgba(168,89,104,.08);}',
    '#lmConsent .lmc-accept{background:#A85968;color:#fff;border-color:#A85968;}',
    '#lmConsent .lmc-accept:hover{background:#8f4555;border-color:#8f4555;}',
    '@media(max-width:640px){#lmConsent .lmc-in{padding:1rem 1.1rem;gap:.9rem;}',
    '#lmConsent .lmc-btns{flex:1 1 100%;}#lmConsent button{flex:1;}}'
  ].join('');

  function inject() {
    if (document.getElementById('lmConsent')) { document.getElementById('lmConsent').classList.add('show'); return; }
    var st = document.createElement('style'); st.id = 'lmConsentStyle'; st.textContent = STYLE;
    document.head.appendChild(st);

    var d = document.createElement('div');
    d.id = 'lmConsent';
    d.setAttribute('role', 'dialog');
    d.setAttribute('aria-label', 'Gestion des cookies');
    d.innerHTML =
      '<div class="lmc-in">'
      + '<p>Nous utilisons des cookies de mesure d\'audience pour améliorer votre expérience. '
      + 'Vous pouvez les accepter ou les refuser. '
      + '<a href="legal.html#confidentialite">En savoir plus</a></p>'
      + '<div class="lmc-btns">'
      + '<button type="button" class="lmc-refuse" id="lmcRefuse">Refuser</button>'
      + '<button type="button" class="lmc-accept" id="lmcAccept">Accepter</button>'
      + '</div></div>';
    document.body.appendChild(d);
    requestAnimationFrame(function () { d.classList.add('show'); });

    document.getElementById('lmcAccept').addEventListener('click', function () {
      setChoice('granted');
      if (window.lumeraInitTracking) window.lumeraInitTracking();
      close();
    });
    document.getElementById('lmcRefuse').addEventListener('click', function () {
      setChoice('denied');
      close();
    });
  }

  function close() {
    var el = document.getElementById('lmConsent');
    if (!el) return;
    el.classList.remove('show');
    setTimeout(function () { if (el && el.parentNode) el.parentNode.removeChild(el); }, 420);
  }

  // Permet de rouvrir la bannière (ex : lien « Cookies » dans le footer)
  window.lumeraOpenConsent = inject;

  // Première visite (aucun choix mémorisé) → on affiche la bannière
  if (!getChoice()) {
    if (document.readyState !== 'loading') inject();
    else document.addEventListener('DOMContentLoaded', inject);
  }
})();
