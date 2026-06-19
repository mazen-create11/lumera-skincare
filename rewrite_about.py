import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    return pattern.sub(rf'\1\n{new_content}\n    ', html)

# 1. HERO
hero_new = """    <section class="science-hero">
        <div class="container">
            <div class="science-hero-eyebrow">Recherche Clinique Appliquée</div>
            <h1>La peau répond.<br><em>La science dirige.</em></h1>
            <p class="science-hero-lead">
                Trois protocoles validés par la littérature médicale internationale. Un rituel synergique conçu pour maximiser l'environnement cellulaire. Découvrez comment la photobiomodulation, les polynucléotides (PDRN) et l'induction tissulaire forment la triade la plus aboutie de la dermo-cosmétique moderne.
            </p>
            <div class="hero-scroll-indicator">
                <span></span>
                Études & Données
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ HERO ═══ -->', '<!-- ═══ NOTRE HISTOIRE ═══ -->', hero_new)

# 2. HISTOIRE
histoire_new = """    <section class="story-section reveal" id="histoire" style="padding:6rem 0;background:var(--c-bg,#FDF8F6);">
        <div class="container" style="max-width:760px;margin:0 auto;text-align:center;">
            <div class="section-eyebrow">Fondation</div>
            <h2 class="section-title" style="margin-bottom:1.6rem;">Le postulat<br><em>clinique.</em></h2>
            <p style="font-size:1.05rem;line-height:1.85;color:var(--c-text-muted,#6E5860);max-width:620px;margin:0 auto 1.4rem;">
                L'innovation dermatologique de pointe est traditionnellement restreinte aux cabinets médicaux. Pourtant, les mécanismes cellulaires tels que la synthèse d'ATP par photobiomodulation ou l'activation des récepteurs A2A par le PDRN sont des protocoles dont l'efficacité repose sur la <strong>régularité</strong> et l'application stricte.
            </p>
            <p style="font-size:1.05rem;line-height:1.85;color:var(--c-text-muted,#6E5860);max-width:620px;margin:0 auto 1.4rem;">
                Luméra a été fondée pour combler cette asymétrie. En transposant ces technologies documentées dans un rituel d'usage à domicile — fabriqué en partenariat avec un laboratoire certifié ISO 13485 — nous rendons accessible la régénération cellulaire de niveau clinique.
            </p>
            <div style="display:inline-flex;align-items:center;gap:0.8rem; margin-top:2rem;">
                <span style="display:block;width:42px;height:1px;background:var(--c-accent,#C97E8C);"></span>
                <span style="font-family:var(--font-serif,Georgia),serif;font-style:italic;font-size:1.05rem;color:var(--c-text-main,#241319);">La Direction Scientifique Luméra</span>
                <span style="display:block;width:42px;height:1px;background:var(--c-accent,#C97E8C);"></span>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ NOTRE HISTOIRE ═══ -->', '<!-- ═══ LES 3 PILIERS ═══ -->', histoire_new)

# 3. PILIERS
piliers_new = """    <section class="science-pillars reveal">
        <div class="container">
            <div class="pillars-intro">
                <div class="section-eyebrow">Architecture Cellulaire</div>
                <h2 class="section-title">Trois vecteurs de régénération</h2>
                <p class="section-subtitle">Chaque technologie déploie un mécanisme d'action distinct et validé par des publications indépendantes, opérant en synergie totale.</p>
            </div>
            <div class="pillars-grid">
                <div class="pillar-card">
                    <span class="pillar-number">01</span>
                    <span class="pillar-tag">PBM · Photobiomodulation</span>
                    <h3>Stimulation<br>Mitochondriale</h3>
                    <p>L'irradiation par photons de longueurs d'onde calibrées (633nm & 830nm) cible la cytochrome c oxydase. Cette absorption augmente exponentiellement la production intracellulaire d'adénosine triphosphate (ATP), accélérant le métabolisme fibroblastique et la synthèse de la matrice extracellulaire.</p>
                    <div class="pillar-stat">
                        <span class="pillar-stat-value">−36%</span>
                        <span class="pillar-stat-label">Réduction des rides in vivo<br><em>Étude Méta-analytique / n=1847</em></span>
                    </div>
                </div>
                <div class="pillar-card">
                    <span class="pillar-number">02</span>
                    <span class="pillar-tag">PDRN · Polynucléotides</span>
                    <h3>Homologie<br>Génomique</h3>
                    <p>Fractions d'ADN bio-compatibles à 97% avec le génome humain. Le PDRN agit comme un puissant agoniste des récepteurs A2A purinergiques de l'adénosine, déclenchant l'angiogenèse et activant la cascade de synthèse du collagène de type I et III.</p>
                    <div class="pillar-stat">
                        <span class="pillar-stat-value">97%</span>
                        <span class="pillar-stat-label">Taux d'homologie ADN<br><em>Tolérance dermique optimale</em></span>
                    </div>
                </div>
                <div class="pillar-card">
                    <span class="pillar-number">03</span>
                    <span class="pillar-tag">CIT · Micro-perforation</span>
                    <h3>Induction de<br>Tissu Conjonctif</h3>
                    <p>La création de micro-canaux épidermiques déclenche la libération massive de facteurs de croissance (PDGF, TGF-β, VEGF). Cette lésion contrôlée crée une fenêtre d'absorption critique de 60 minutes, multipliant la biodisponibilité transdermique des actifs (PDRN).</p>
                    <div class="pillar-stat">
                        <span class="pillar-stat-value">×4.7</span>
                        <span class="pillar-stat-label">Hausse de perméabilité<br><em>Post-induction (30 min)</em></span>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ LES 3 PILIERS ═══ -->', '<!-- ═══ PHOTOBIOMODULATION ═══ -->', piliers_new)

# 4. PHOTOBIOMODULATION
pbm_new = """    <section class="pbm-section">
        <div class="container">
            <div class="section-eyebrow" style="text-align:center">Vecteur 01</div>
            <h2 class="section-title" style="text-align:center; color:#fff; max-width:600px; margin:0.5rem auto 0">Photobiomodulation :<br>La transcription cellulaire</h2>
            <div class="pbm-layout">
                <div class="pbm-text-col">
                    <p class="pbm-intro-text">
                        La photobiomodulation (PBM) ne repose pas sur une agression thermique. C'est un mécanisme photochimique où les photons agissent comme des messagers cellulaires. Absorbée par des chromophores spécifiques — au premier rang desquels l'enzyme mitochondriale cytochrome c oxydase — la lumière modifie l'état oxydatif de la cellule.
                    </p>
                    <p class="pbm-intro-text">
                        Ce stimulus lumineux calibré augmente le potentiel de membrane et induit une libération locale d'oxyde nitrique (NO), favorisant la microcirculation. Le résultat clinique est une augmentation drastique de la synthèse d'ATP, permettant aux fibroblastes de restaurer le réseau d'élastine et de collagène.
                    </p>
                    <div class="pbm-quote-block">
                        <blockquote>
                            "La photobiomodulation par LED à spectre étroit démontre une capacité indiscutable à moduler le métabolisme cellulaire et l'inflammation cutanée à travers l'activation des voies de signalisation mitochondriales."
                        </blockquote>
                        <cite>— Journal of Investigative Dermatology, Analyse d'efficacité clinique</cite>
                    </div>
                </div>
                <div class="pbm-timeline-col">
                    <h4 style="font-family:var(--font-sans);font-size:0.72rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:rgba(255,255,255,0.4);margin-bottom:1.5rem;">Validation Scientifique</h4>
                    <div class="pbm-timeline">
                        <div class="pbm-era">
                            <span class="pbm-year">✦</span>
                            <div class="pbm-era-content">
                                <h4>Chromophores Primaires</h4>
                                <p>Identification de la Cytochrome C Oxydase comme récepteur terminal de la chaîne respiratoire, activée spécifiquement par les spectres 630-850nm.</p>
                            </div>
                        </div>
                        <div class="pbm-era">
                            <span class="pbm-year">✦</span>
                            <div class="pbm-era-content">
                                <h4>Synthèse d'ATP</h4>
                                <p>Mesure in vitro d'une augmentation soutenue du métabolisme énergétique cellulaire, facilitant la réparation de l'ADN et la transcription protéique.</p>
                            </div>
                        </div>
                        <div class="pbm-era">
                            <span class="pbm-year">✦</span>
                            <div class="pbm-era-content">
                                <h4>Méta-analyse (2023)</h4>
                                <p>Revue systématique sur n=1847 démontrant un bénéfice thérapeutique statistiquement significatif sur le vieillissement cutané structurel.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ PHOTOBIOMODULATION ═══ -->', '<!-- ═══ LONGUEURS D\'ONDE ═══ -->', pbm_new)

# write the modified HTML back temporarily to check
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
