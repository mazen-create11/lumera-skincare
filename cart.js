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

  // Cross-sell intelligent : coffret si produits à l'unité (et pas déjà le coffret),
  // recharge sérum si le coffret est là, masqué sinon. Injecté sur toutes les pages.
  function updateUpsell(c) {
    var hasCoffret = c.some(function (i) { return isCoffret(i.name); });
    var hasUnit = c.some(function (i) { return !isCoffret(i.name); });
    var mode = (c.length && hasUnit && !hasCoffret) ? 'coffret' : (c.length && hasCoffret ? 'serum' : null);
    document.querySelectorAll('.cart-footer').forEach(function (f) {
      var drawer = f.parentNode;
      var up = drawer.querySelector('.cart-upsell');
      if (!mode) { if (up) up.style.display = 'none'; return; }
      if (!up) { up = document.createElement('div'); up.className = 'cart-upsell'; drawer.insertBefore(up, f); }
      up.style.display = '';
      if (mode === 'coffret') {
        up.innerHTML = '<img src="assets/coffret-closed.webp" alt="Coffret Le Rituel Complet" style="width:54px;height:54px;object-fit:cover;border-radius:10px">'
          + '<div class="cart-upsell-info"><h4>Passez au Rituel · économisez 50 €</h4><p>Les 3 soins réunis — <strong>279,97 €</strong> <s style="color:var(--c-text-light)">329,97 €</s></p></div>'
          + '<a href="bundle.html" class="add-upsell">Voir</a>';
      } else {
        up.innerHTML = '<img src="assets/card-serum.webp" alt="Sérum PDRN" style="width:54px;height:54px;object-fit:cover;border-radius:10px">'
          + '<div class="cart-upsell-info"><h4>Complétez votre rituel</h4><p>Sérum PDRN — recharge · <strong>39,99 €</strong></p></div>'
          + '<button class="add-upsell" onclick="addToCart(\'Sérum PDRN Glass Skin\',39.99,\'assets/card-serum.webp\')">+ Ajouter</button>';
      }
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
        items.innerHTML = '<div><p style="font-family:var(--font-serif);font-size:1.15rem;color:var(--c-text-muted);margin-bottom:0.4rem;">Votre panier est vide</p><p style="font-size:0.82rem;color:var(--c-text-light);">Découvrez nos rituels signature.</p></div>';
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
    if (fill) fill.style.width = Math.min(100, Math.round(t2 / FREE_SHIP * 100)) + '%';
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
  };
  window.closeCart = function () {
    var o = document.querySelector('.cart-overlay'), d = document.getElementById('cartDrawer');
    if (o) o.classList.remove('active'); if (d) d.classList.remove('active');
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
