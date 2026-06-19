import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n    ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

# Replace RESULTS section
results_new = """    <div class="container">
        <div class="results-head reveal">
            <span class="eyebrow">Littérature Médicale</span>
            <h2 class="h2">Évidences<br><em>cliniques.</em></h2>
            <p class="sub">Chaque donnée est extraite de publications indépendantes mesurant l'impact in vivo de nos 3 technologies (PBM, PDRN, CIT) sur la structure dermique.</p>
        </div>

        <div class="ba-cards reveal">
            <article class="ba-card">
                <div class="ba-media">
                    <img loading="lazy" src="assets/ba-1.webp" alt="Avant après rides masque led lumera">
                    <span class="ba-tag before">J+0</span>
                    <span class="ba-tag after">J+84</span>
                </div>
                <div class="ba-cap">
                    <strong>−36% Sillon Nasogénien</strong>
                    <span>Diminution de la profondeur des rides. <em>(Méta-analyse sur n=1847)</em></span>
                </div>
            </article>
            <article class="ba-card">
                <div class="ba-media">
                    <img loading="lazy" src="assets/ba-2.webp" alt="Avant après fermeté lumera">
                    <span class="ba-tag before">J+0</span>
                    <span class="ba-tag after">J+56</span>
                </div>
                <div class="ba-cap">
                    <strong>+19% Élasticité Cutanée</strong>
                    <span>Augmentation de la tension tissulaire mesurée par cutomètre.</span>
                </div>
            </article>
            <article class="ba-card">
                <div class="ba-media">
                    <img loading="lazy" src="assets/ba-3.webp" alt="Avant après acné lumera">
                    <span class="ba-tag before">J+0</span>
                    <span class="ba-tag after">J+84</span>
                </div>
                <div class="ba-cap">
                    <strong>−53% État Inflammatoire</strong>
                    <span>Réduction du grade lésionnel. <em>(PBM 470nm, n=86)</em></span>
                </div>
            </article>
        </div>

        <div class="results-grid reveal">
            <div class="results-img"><img loading="lazy" src="assets/results-portrait.webp" alt="Résultats Luméra Skincare sur la peau"></div>
            <div>
                <h3 class="h2" style="font-size:clamp(1.8rem, 3vw, 2.4rem); margin-bottom:1.5rem">Architecture de<br><em>régénération.</em></h3>
                <p style="font-size:1.05rem; line-height:1.8; color:var(--text-mid)">
                    Luméra ne traite pas la surface de l'épiderme. Le protocole module le comportement cellulaire profond. L'association PDRN et Photobiomodulation stimule la <strong>Cytochrome c oxydase</strong> et active les <strong>récepteurs A2A</strong> fibroblastiques.
                </p>
                <div class="results-stats">
                    <div class="stat">
                        <span class="v lnum">−36%</span>
                        <span class="l">Profondeur des rides</span>
                        <span class="s">Étude in vivo 12 sem.</span>
                    </div>
                    <div class="stat">
                        <span class="v lnum">+19%</span>
                        <span class="l">Indice d'élasticité</span>
                        <span class="s">Cutométrie 8 sem.</span>
                    </div>
                    <div class="stat">
                        <span class="v lnum">+47%</span>
                        <span class="l">Synthèse Collagène</span>
                        <span class="s">In vitro (PDRN 72h)</span>
                    </div>
                </div>
                <div class="results-disclaimer">Source : Revue Systématique 2023 (PMID: 37128566) &amp; Études indépendantes.</div>
            </div>
        </div>
    </div>"""
html = replace_section(html, '<!-- RESULTS -->\n<section class="sec results">', '<!-- RITUAL -->', results_new)

# Replace RITUAL section
ritual_new = """    <div class="container">
        <div class="sec-head reveal">
            <span class="eyebrow">Synergie</span>
            <h2 class="h2">Protocole<br><em>clinique séquencé.</em></h2>
            <p class="sub">Trois vecteurs bio-compatibles opérant en parfaite chronologie pour contourner la barrière lipophile épidermique.</p>
        </div>
        <div class="steps">
            <div class="step reveal">
                <div class="step-top">
                    <span class="step-num lnum">I</span>
                    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
                </div>
                <h4>L'Induction (CIT)</h4>
                <p>Création de micro-canaux à 0,25 mm. Déclenche la libération de facteurs de croissance (PDGF, TGF-β) et augmente la perméabilité cutanée par ×4.7.</p>
                <span class="step-time lnum">T0 · 5 Min</span>
            </div>
            <div class="step reveal">
                <div class="step-top">
                    <span class="step-num lnum">II</span>
                    <svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <h4>L'Infusion (PDRN)</h4>
                <p>Application immédiate du Sérum à 1% de PDRN dans la fenêtre d'ouverture transdermique (60 min). Activation des récepteurs A2A.</p>
                <span class="step-time lnum">T+5 · Immédiat</span>
            </div>
            <div class="step reveal">
                <div class="step-top">
                    <span class="step-num lnum">III</span>
                    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
                </div>
                <h4>La Photomodulation</h4>
                <p>Irradiation LED (630nm/840nm) inondant la matrice d'ATP mitochondrial pour alimenter la prolifération cellulaire initiée par le PDRN.</p>
                <span class="step-time lnum">T+10 · 20 Min</span>
            </div>
        </div>
    </div>"""
html = replace_section(html, '<!-- RITUAL -->\n<section class="sec ritual">', '<!-- WHY -->', ritual_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
