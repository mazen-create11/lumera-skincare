/* Panier partagé Luméra — localStorage, accumulation, total réel, persistant entre pages */
(function () {
  var KEY = 'lumera_cart';
  function get() { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } }
  function save(c) { localStorage.setItem(KEY, JSON.stringify(c)); }
  function count(c) { return c.reduce(function (n, i) { return n + i.qty; }, 0); }
  function total(c) { return c.reduce(function (t, i) { return t + i.price * i.qty; }, 0); }

  function fmt(n) { return (Math.round(n * 100) / 100).toFixed(2).replace('.', ',').replace(',00', '') + ' €'; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function attr(s) { return String(s).replace(/'/g, "\\'"); }

  // Image de repli si l'item n'a pas d'image (robustesse panier)
  function imgFor(name, img) {
    if (img) return img;
    var n = String(name).toLowerCase();
    if (/masque|mask/.test(n)) return 'assets/card-mask.webp';
    if (/s[ée]rum/.test(n)) return 'assets/card-serum.webp';
    if (/stylo|pen|needl/.test(n)) return 'assets/card-pen.webp';
    if (/rituel|coffret/.test(n)) return 'assets/coffret-closed.webp';
    return 'assets/coffret-closed.webp';
  }
  function isCoffret(name) { return /rituel|coffret/i.test(name); }
  function isMask(name) { return !isCoffret(name) && /masque|mask/i.test(name); }
  function isSerum(name) { return !isCoffret(name) && /s[ée]rum/i.test(name); }
  function isPen(name) { return !isCoffret(name) && /stylo|pen|needl/i.test(name); }

  // Catalogue canonique (pour les suggestions du panier)
  var CATALOG = {
    coffret: { name: 'Le Rituel Complet', price: 279.97, img: 'assets/coffret-open.webp?v=12' },
    mask: { name: 'Masque LED Face + Cou', price: 249.99, img: 'assets/card-mask.webp', note: 'Visage + cou' },
    serum: { name: 'Sérum PDRN Glass Skin', price: 39.99, img: 'assets/card-serum.webp', note: 'Régénération intense' },
    pen: { name: 'Stylo Micro-needling', price: 39.99, img: 'assets/card-pen.webp', note: 'Absorption ×4' }
  };

  // Moteur de cross-sell contextuel : ne jamais reproposer ce qu'on a,
  // monter vers le coffret depuis un produit seul, proposer une recharge si le coffret est là.
  function suggestionsFor(c) {
    if (!c.length) return null;
    var hasCoffret = c.some(function (i) { return isCoffret(i.name); });
    var hasMask = c.some(function (i) { return isMask(i.name); });
    var hasSerum = c.some(function (i) { return isSerum(i.name); });
    var hasPen = c.some(function (i) { return isPen(i.name); });
    if (hasCoffret) {
      // Coffret déjà pris : réappro consommable pour la suite (pas de produits déjà inclus)
      return { title: 'Pensez à la suite', items: [
        { name: CATALOG.serum.name, price: CATALOG.serum.price, img: CATALOG.serum.img, note: 'Recharge — pour ne jamais en manquer' }
      ] };
    }
    // Produit(s) à l'unité : on monte vers le coffret (éco) + on complète avec les soins manquants
    var items = [{ name: CATALOG.coffret.name, price: CATALOG.coffret.price, img: CATALOG.coffret.img, note: 'Les 3 soins réunis · économisez 50 €' }];
    if (!hasMask) items.push(CATALOG.mask);
    if (!hasSerum) items.push(CATALOG.serum);
    if (!hasPen) items.push(CATALOG.pen);
    return { title: 'Complétez votre rituel', items: items.slice(0, 3) };
  }

  // Cross-sell intelligent : coffret si produits à l'unité (et pas déjà le coffret),
  // recharge sérum si le coffret est là, masqué sinon. Injecté sur toutes les pages.
  function updateUpsell(c) {
    var sug = suggestionsFor(c);
    document.querySelectorAll('.cart-footer').forEach(function (f) {
      var drawer = f.parentNode;
      var up = drawer.querySelector('.cart-upsell');
      if (!sug || !sug.items.length) { if (up) up.style.display = 'none'; return; }
      if (!up) { up = document.createElement('div'); up.className = 'cart-upsell'; drawer.insertBefore(up, f); }
      up.style.display = '';
      up.innerHTML = '<p class="cart-upsell-h">' + esc(sug.title) + '</p>' + sug.items.map(function (s) {
        var note = s.note ? '<em class="lm-sug-note">' + esc(s.note) + '</em>' : '';
        return '<div class="lm-sug"><img src="' + s.img + '" alt="' + esc(s.name) + '">'
          + '<div class="lm-sug-info"><span class="lm-sug-n">' + esc(s.name) + '</span>'
          + '<span class="lm-sug-p">' + fmt(s.price) + (note ? ' · ' + note : '') + '</span></div>'
          + '<button class="lm-sug-add" aria-label="Ajouter ' + esc(s.name) + '" onclick="addToCart(\'' + attr(s.name) + '\',' + s.price + ',\'' + s.img + '\')">+</button></div>';
      }).join('');
    });
  }

  function render() {
    var c = get();
    document.querySelectorAll('.cart-btn').forEach(function (b) { b.textContent = 'Panier (' + count(c) + ')'; });
    var items = document.getElementById('cartItems') || document.querySelector('.cart-items');
    if (items) {
      if (c.length) {
        items.classList.remove('is-empty');
        items.innerHTML = c.map(function (i) {
          var a = attr(i.name), n = esc(i.name);
          return '<div class="ci-row">'
            + '<img class="ci-thumb" src="' + esc(imgFor(i.name, i.img)) + '" alt="' + n + '">'
            + '<div class="ci-info">'
            + '<div class="ci-head"><span class="ci-name">' + n + '</span>'
            + '<button class="ci-remove" onclick="lumeraRemove(\'' + a + '\')">Retirer</button></div>'
            + '<span class="ci-unit">' + fmt(i.price) + ' l’unité</span>'
            + '<div class="ci-controls">'
            + '<span class="ci-stepper"><button aria-label="Diminuer" onclick="lumeraQty(\'' + a + '\',-1)">−</button>'
            + '<span>' + i.qty + '</span>'
            + '<button aria-label="Augmenter" onclick="lumeraQty(\'' + a + '\',1)">+</button></span>'
            + '<span class="ci-line">' + fmt(i.price * i.qty) + '</span>'
            + '</div></div></div>';
        }).join('');
      } else {
        items.classList.add('is-empty');
        var sug = [
          ['Le Rituel Complet', 279.97, 'assets/coffret-open.webp?v=12'],
          ['Masque LED Face + Cou', 249.99, 'assets/card-mask.webp'],
          ['Sérum PDRN Glass Skin', 39.99, 'assets/card-serum.webp'],
          ['Stylo Micro-needling', 39.99, 'assets/card-pen.webp']
        ];
        var rows = sug.map(function (s) {
          return '<div class="lm-sug"><img src="' + s[2] + '" alt="' + esc(s[0]) + '">'
            + '<div class="lm-sug-info"><span class="lm-sug-n">' + esc(s[0]) + '</span><span class="lm-sug-p">' + fmt(s[1]) + '</span></div>'
            + '<button class="lm-sug-add" aria-label="Ajouter ' + esc(s[0]) + '" onclick="addToCart(\'' + attr(s[0]) + '\',' + s[1] + ',\'' + s[2] + '\')">+</button></div>';
        }).join('');
        items.innerHTML = '<div class="lm-empty">'
          + '<div class="lm-empty-ic"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l1.6 1.6M17.4 17.4 19 19M19 5l-1.6 1.6M6.6 17.4 5 19"/><circle cx="12" cy="12" r="3.2"/></svg></div>'
          + '<p class="lm-empty-t">Votre panier vous attend</p>'
          + '<p class="lm-empty-s">Composez votre rituel lumière. Livraison offerte et 30 jours pour l’adopter.</p>'
          + '<div class="lm-suggest"><p class="lm-suggest-h">Nos rituels signature</p>' + rows + '</div></div>';
      }
    }
    var tot = document.getElementById('cartTotal') || document.querySelector('.cart-total span:last-child');
    if (tot) tot.textContent = fmt(total(c));
    var co = document.getElementById('checkoutBtn') || document.querySelector('.cart-footer .btn-solid, .cart-footer button');
    if (co) { var on = c.length > 0; co.disabled = !on; co.style.opacity = on ? '1' : '0.5'; co.style.pointerEvents = on ? 'auto' : 'none'; co.onclick = window.lumeraCheckout; }
    var FREE_SHIP = 0, t2 = total(c);
    var prog = document.querySelector('.cart-progress p');
    if (prog) prog.innerHTML = 'Livraison offerte incluse ✦';
    var fill = document.querySelector('.progress-bar-fill');
    if (fill && FREE_SHIP > 0) fill.style.width = Math.min(100, Math.round(t2 / FREE_SHIP * 100)) + '%';
    if (co && c.length) co.textContent = 'Commander en toute sécurité';
    // Réassurance panier (3× sans frais + trust) — injectée une seule fois par footer
    document.querySelectorAll('.cart-footer').forEach(function (f) {
      if (f.querySelector('.cart-reassure')) return;
      var d = document.createElement('div');
      d.className = 'cart-reassure';
      d.style.cssText = 'margin:0.5rem 0 0.2rem;';
      var ic = function (p) { return '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="#B07E89" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0">' + p + '</svg>'; };
      var icLock = ic('<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>');
      var icShield = ic('<path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>');
      var icTruck = ic('<path d="M3 7h11v8H3z"/><path d="M14 10h4l3 3v2h-7z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17.5" cy="18" r="1.6"/>');
      d.innerHTML = '<p style="font-size:0.76rem;color:#A85968;font-weight:600;text-align:center;margin:0 0 0.6rem;">ou 3× sans frais dès 100 € — sans intérêts</p>'
        + '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:0.45rem 1rem;font-size:0.68rem;color:#8A6A72;font-weight:500;">'
        + '<span style="display:inline-flex;align-items:center;gap:0.3rem;">' + icLock + 'Paiement sécurisé</span>'
        + '<span style="display:inline-flex;align-items:center;gap:0.3rem;">' + icShield + '30 j satisfaite ou remboursée</span>'
        + '<span style="display:inline-flex;align-items:center;gap:0.3rem;">' + icTruck + 'Livraison offerte</span></div>';
      var btn = f.querySelector('button, .btn');
      if (btn) f.insertBefore(d, btn); else f.appendChild(d);
    });
    updateUpsell(c);
  }

  window.openCart = function () {
    var o = document.querySelector('.cart-overlay'), d = document.getElementById('cartDrawer');
    if (o) { o.classList.add('active'); o.style.userSelect = 'none'; o.style.webkitUserSelect = 'none'; }
    if (d) d.classList.add('active');
    document.body.style.overflow = 'hidden';
    var items = document.getElementById('cartItems') || document.querySelector('.cart-items');
    if (items) { items.classList.remove('lm-stagger'); void items.offsetWidth; items.classList.add('lm-stagger'); }
  };
  window.closeCart = function () {
    var o = document.querySelector('.cart-overlay'), d = document.getElementById('cartDrawer');
    if (o) o.classList.remove('active'); if (d) d.classList.remove('active');
    document.body.style.overflow = '';
  };
  window.addToCart = function (name, price, img) {
    var c = get(), ex = c.find(function (i) { return i.name === name; });
    if (ex) ex.qty++; else c.push({ name: name, price: Number(price) || 0, img: img || '', qty: 1 });
    save(c); render(); window.openCart();
    if (window.lumeraTrack) lumeraTrack('add_to_cart', { value: Number(price) || 0, name: name });
  };
  window.lumeraRemove = function (name) {
    save(get().filter(function (i) { return i.name !== name; })); render();
  };
  window.lumeraQty = function (name, delta) {
    var c = get(), it = c.find(function (i) { return i.name === name; });
    if (!it) return;
    it.qty += delta;
    if (it.qty < 1) c = c.filter(function (i) { return i.name !== name; });
    save(c); render();
  };

  // Checkout — prise de commande par e-mail avec récap (lien de paiement envoyé en retour).
  // Pour brancher Stripe plus tard : remplacer le corps par window.location.href = '<Payment Link>'.
  window.lumeraCheckout = function () {
    var c = get();
    if (!c.length) return;
    if (window.lumeraTrack) lumeraTrack('begin_checkout', { value: total(c) });
    var lines = c.map(function (i) { return '- ' + i.qty + ' x ' + i.name + '  (' + fmt(i.price) + ' l\'unite)  = ' + fmt(i.price * i.qty); }).join('\n');
    var tot = fmt(total(c));
    var subject = 'Commande Lumera — ' + tot;
    var body = 'Bonjour Lumera,\n\nJe souhaite passer commande :\n\n' + lines
      + '\n\nTotal : ' + tot + '\nLivraison offerte · 30 jours satisfaite ou remboursee\n\n'
      + 'Mes coordonnees de livraison :\nNom & prenom : \nAdresse complete : \nCode postal / Ville : \nTelephone : \n\n'
      + 'Merci de m\'envoyer le lien de paiement securise pour finaliser ma commande. A tres vite !';
    window.location.href = 'mailto:contact@lumera-skincare.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  };

  if (document.readyState !== 'loading') render();
  else document.addEventListener('DOMContentLoaded', render);

  // Auto-ouverture rétention intelligente
  window.addEventListener('load', function() {
    var c = get();
    if (c.length > 0 && !sessionStorage.getItem('lumera_retention_shown')) {
      sessionStorage.setItem('lumera_retention_shown', 'true');
      setTimeout(function() {
        if(window.openCart) window.openCart();
      }, 1800); // 1.8s de délai naturel avant affichage
    }
  });

  // UX Feedback : Bouton d'ajout au panier
  document.addEventListener('click', function(e) {
    var btn = e.target.closest('button[onclick^="addToCart"]');
    if (btn) {
      var oldHtml = btn.innerHTML;
      btn.innerHTML = 'Ajouté ! ✓';
      btn.style.pointerEvents = 'none';
      setTimeout(function() {
        btn.innerHTML = oldHtml;
        btn.style.pointerEvents = 'auto';
      }, 1500);
    }
  });
})();
