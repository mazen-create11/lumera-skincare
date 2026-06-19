# BRIEF — Reprise du projet LUMÉRA (pour Gemini / Antigravity)

> Tu reprends un site e-commerce premium construit jusqu'ici par Claude. Le patron (Mazen) te confie le projet **pour voir ce que tu fais de mieux**. Lis tout, puis fais le travail demandé en bas (section « TA MISSION »). Antigravity te donne un **navigateur intégré : sers-t'en pour VOIR le site et juger les images en vrai.**

---

## 1. Le projet en 30 secondes
**Luméra** = marque française de skincare premium. Produit phare : un **masque LED visage + cou en silicone souple**, vendu avec un **sérum PDRN** et un **stylo de microneedling**. Positionnement : « le rituel des cliniques esthétiques, à la maison », anti-âge, éclat, fermeté.

**Objectif du site** : un **e-commerce DTC qui convertit fort, mais haut de gamme** (références mentales : La Mer, Augustinus Bader, Dior Beauté). Pas un site « cheap dropshipping ».

**Produits & prix réels (à respecter, ne pas inventer) :**
- Masque LED Face + Cou — **249 €**
- Sérum PDRN « Glass Skin » — **49 €** (35 ml)
- Stylo Micro-needling 0,25 mm — **29 €**
- **Le Rituel Complet** (les 3 + guide) — **289 €** (au lieu de 327 €, soit −38 €)

---

## 2. Stack technique
- **Vanilla HTML/CSS/JS**, zéro framework, zéro build. Chaque page = un `.html`.
- CSS : une feuille partagée **`styles.css`** (tokens `--c-*`, layout commun) + un bloc `<style>` inline propre à chaque page (surtout `index.html`).
- JS : **`scripts.js`** (partagé), **`cart.js`** (panier en localStorage), + petits scripts inline par page.
- **Panier** : `addToCart(nom, prix, image)` → localStorage, drawer latéral. Pas de backend.
- **Checkout** : pas encore branché (Stripe à venir, bloqué côté admin sur le SIRET — hors scope dev).

**Lancer le site en local :**
```bash
cd ~/.gemini/antigravity/scratch/lumera-skincare
python3 -m http.server 8848
# puis ouvrir http://localhost:8848/index.html
```

**Pages :** `index.html` (home), `product-mask.html`, `product-serum.html`, `product-pen.html`, `bundle.html` (Le Rituel), `about.html` (science), `tiktok.html`, `contact.html`, `livraison.html`, `legal.html`.

**Fichiers temporaires à SUPPRIMER avant livraison finale :** `_view.html`, `_ccheck.html` (outils de QA Claude).

---

## 3. La Direction Artistique (DA) — à garder et sublimer
- **Palette rosé premium**, chaud, doux. Tokens clés dans `index.html` : `--cream #FDF8F6`, `--blush #F7EDE9`, `--rose #C97E8C`, `--rose-dark #A85968`, `--ink #2A1418`, `--gold #B98E5E`. Dans `styles.css` : `--c-bg`, `--c-surface`, `--c-text-main #241319`, `--c-text-muted`, `--c-accent`, `--c-accent-dark #9C5263`, `--c-border`, `--c-gold`.
- **Typo** : titres en **Cormorant Garamond** (serif élégant, italique pour les accents), texte en **DM Sans**.
- **Règle d'or DA** : rosé **légèrement** poudré, jamais blanc froid, jamais « candy pink » criard. Ambiance institut de luxe : marbre crème, roses dusty-rose, lumière chaude.
- **Accessibilité** : viser **WCAG AA** (contraste texte ≥ 4.5:1). `bundle.html` est déjà à 100/100. ⚠️ Piège connu : axe-core compte l'**opacité héritée** d'un parent (ex. `opacity:.65` sur un bloc baisse le contraste effectif du texte).

---

## 4. Les VISUELS — méthode imposée (très important)
Le patron a **horreur des rendus IA génériques / candy-pink**. Règle stricte, répétée 3 fois :

> **Toujours partir des VRAIES photos produits du dossier `assets/`** et générer de **nouveaux angles en image-to-image**, en gardant la forme / couleur / label EXACTS du produit. **Jamais** de génération « from scratch » en text-to-image (ça invente un autre produit = rejeté).

**Le vrai produit (à reconnaître sur les assets) :** masque LED **silicone ROSE texturé, souple, visage + cou**, contour des yeux **doré/rose-gold** ; fiole sérum **« AFCARE PDRN ESSENCE AMPOULES »** ; stylo microneedling **rose** à écran. (Ce n'est PAS une coque rigide rose-gold.)

**Outil image utilisé par Claude (Higgsfield CLI, ~789 crédits dispo) :**
```bash
higgsfield generate create nano_banana_2 \
  --image assets/<vraie_photo>.webp \
  --prompt "garder le produit EXACT, recomposer en scène premium marbre/roses, DA blush" \
  --aspect_ratio 4:5 --resolution 4k --wait
```
- `nano_banana_2` (Nano Banana Pro) = **image-to-image** (fidélité produit). `gpt_image_2` (GPT Image 2, 4K) = scènes from-scratch (à éviter pour le produit).
- **Piège technique** : `sips -s format webp` **échoue en silence** sur ce Mac → utiliser **`cwebp -q 86 -resize 1240 0 in.png -o out.webp`**, et vérifier les dimensions après. Toujours **bumper `?v=N`** sur le `src` pour casser le cache navigateur.

> Tu peux régénérer des visuels si tu fais mieux — **mais via image-to-image depuis les vraies photos**, et **juge le rendu dans ton navigateur intégré avant de l'intégrer**.

---

## 5. Ce qui est DÉJÀ fait (par Claude)
- **`bundle.html`** : poli à fond, a11y 100/100, paiement 3×, bandeau garanties, comparatif prix, vidéo différée (perf).
- **`styles.css`** : passes a11y (tokens contrastés, footer, icônes paiement, `--c-accent-dark`), + classe sticky `.satc` partagée.
- **`index.html` (home) — couche conversion DTC posée :**
  - Hero « commercial » : prix `289 € / ~~327 €~~ / Économisez 38 €` + bouton **Ajouter au panier** + ligne **3× 96,33 €** + bénéfices en ✓.
  - **Bandeau confiance** (4 icônes : livraison / 3× / 30 j / France).
  - **Cartes produit** avec **achat rapide** (prix + bouton « Ajouter »).
  - **Barre sticky add-to-cart** (apparaît après le hero, masquée sur le footer).
  - **Comparatif Luméra vs masques rigides** (données honnêtes, note de transparence).
  - **Section garantie sombre** (« Essayez 30 jours. Le risque est pour nous. » + 3 réassurances).
  - **Visuels hero + bloc coffret REFAITS** depuis les vraies photos (`coffret-hero.webp?v=3`, `coffret-featured.webp?v=3`) — premium, DA respectée.
- **Pages produit (masque/sérum/stylo)** : **barre sticky add-to-cart** ajoutée.

⚠️ **Collision CSS à connaître** : `styles.css` définit déjà `.guarantee-inner`, `.guarantee-section`, `.mission-inner`, `.science-inner`, `.expert-inner`, `.story-inner` en `display:grid`. **Préfixer toute nouvelle classe** (Claude a utilisé `.lmg-inner` pour la garantie de la home) sinon layout cassé. Vérifier `grep "<nom>" styles.css` avant de nommer.

---

## 6. Ce qui RESTE / points faibles connus
1. **`about.html` et `index.html`** : un `sed` global `accent → accent-dark` a **assombri certains labels sur fond sombre** (`.eyebrow`/`.section-eyebrow` peu lisibles sur blocs foncés). Besoin d'un passage **contextuel** (accent-dark sur clair, accent/accent-light sur sombre). **NE PAS** refaire de sed global.
2. **Pages produit** : 1 nœud de contraste non localisé (~93/100 a11y) + galerie droite trop haute sur certaines (déséquilibre layout).
3. **Visuels non encore refaits** : `coffret-banner.webp` (bannière home) et `coffret-macro.webp` (section « pourquoi », fond sombre un peu hors-DA) → candidats à régénérer en premium.
4. **Avis vérifiés** : structure pas encore construite. **Contrainte légale stricte** : marque récente, **pas de faux avis ni fausse presse** (DGCCRF/FTC). On peut préparer la STRUCTURE, mais avec de vrais retours seulement.
5. **a11y** non audité sur : `tiktok`, `contact`, `legal`, `livraison`.

---

## 7. Contraintes non négociables
- **Respecter le produit réel** (forme, textes, prix) — ne rien inventer.
- **DA rosé premium** — pas de blanc froid, pas de candy-pink, pas de rendu IA cheap.
- **Légal** : aucun faux avis, fausse note, fausse presse, faux stock/timer. Chiffres réels uniquement.
- **Pas de credentials en dur**, pas de dépendance externe non vérifiée.
- Le patron surveille les coûts : **efficace, va au bout du 1er coup**, vérifie (lint visuel + a11y) avant de dire « fini ».

---

## 8. TA MISSION (ce que le patron attend de toi, Gemini)
Le patron te met sur le projet **exprès pour voir ce que tu proposes en premium et ce que tu fais mieux que Claude.** Il veut un **très, très gros boulot**, pas un coup d'œil. Concrètement :

1. **Ouvre le site dans ton navigateur intégré** et parcours TOUTES les pages (desktop + mobile).
2. **Audit DA** : la direction artistique est-elle vraiment premium et cohérente ? Qu'est-ce qui fait « cheap » ou daté ? Propose des améliorations concrètes (typo, espacements, couleurs, rythme des sections, micro-animations).
3. **Audit images, une par une** : pour **chaque visuel**, dis clairement **« celle-ci va / celle-ci ne va pas »** et **pourquoi** (forme produit, lumière, cohérence DA, artefacts IA). Régénère les mauvaises **en image-to-image depuis les vraies photos** (cf. §4) et **vérifie le rendu dans ton navigateur avant de l'intégrer**.
4. **Bugs & détails** : repère et corrige les bugs (CSS, responsive, a11y, liens morts, incohérences de prix/texte). Soigne les détails que Claude a pu laisser (cf. §6).
5. **Conversion** : propose ce qui manque encore pour convertir mieux (toujours **honnête / légal**).
6. **Livrable** : à la fin, donne au patron un **rapport clair** — ce que tu as changé, ce qui ne va toujours pas, et tes recommandations premium. Montre-lui **ce que tu apportes en plus.**

> Vérifie tout dans le navigateur, ne te fie pas au code seul. Le patron juge sur le **rendu réel**, pas sur les promesses. Bonne chance — montre ce que tu vaux. 🚀

---
*Brief rédigé par Claude (Opus 4.8) le 16 juin 2026 — passation propre du projet Luméra.*
