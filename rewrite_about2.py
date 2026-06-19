import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    return pattern.sub(rf'\1\n{new_content}\n    ', html)

# 5. LONGUEURS D'ONDE
wl_new = """    <section class="wavelength-section reveal">
        <div class="container">
            <div class="wavelength-intro">
                <div class="section-eyebrow">Pénétration Optique</div>
                <h2 class="section-title">Calibration spectrale</h2>
                <p class="section-subtitle">Chaque longueur d'onde est calibrée en nanomètres (nm) pour cibler des couches dermiques spécifiques, de l'épiderme basal au derme réticulaire profond.</p>
            </div>
            <div class="wl-grid">
                <div class="wl-card">
                    <div class="wl-dot-lg" style="background:#D4504A;">630</div>
                    <div class="wl-nm">630 nm</div>
                    <div class="wl-name">Rouge Visible</div>
                    <p>Absorption maximale par l'épiderme basal et le derme papillaire. Cible les kératinocytes pour l'uniformité du teint et les fibroblastes superficiels pour la régénération de la matrice.</p>
                    <div class="wl-evidence">Étude clinique : −36% rides apparentes (12 semaines)</div>
                </div>
                <div class="wl-card">
                    <div class="wl-dot-lg" style="background:#8B5CF6;">840</div>
                    <div class="wl-nm">840 nm</div>
                    <div class="wl-name">Proche Infrarouge (NIR)</div>
                    <p>Pénétration transcutanée atteignant le derme réticulaire. Favorise la prolifération vasculaire (angiogenèse) et la synthèse de faisceaux épais de collagène de type I.</p>
                    <div class="wl-evidence">Étude clinique : +19% élasticité cutanée (8 semaines)</div>
                </div>
                <div class="wl-card">
                    <div class="wl-dot-lg" style="background:#6E1023;">1072</div>
                    <div class="wl-nm">1072 nm</div>
                    <div class="wl-name">Infrarouge Profond</div>
                    <p>Atteint la jonction dermo-hypodermique. Cette longueur d'onde unique module l'expression des gènes pro-inflammatoires et agit sur la restructuration profonde des tissus adipeux sous-cutanés.</p>
                    <div class="wl-evidence">Indication : Restructuration tissulaire avancée</div>
                </div>
            </div>
        </div>
    </section>"""
html = replace_section(html, "<!-- ═══ LONGUEURS D\'ONDE ═══ -->", '<!-- ═══ PDRN ═══ -->', wl_new)

# 6. PDRN
pdrn_new = """    <section class="pdrn-section">
        <div class="container">
            <div class="section-eyebrow">Vecteur 02</div>
            <div class="pdrn-layout">
                <div class="pdrn-info-col reveal-left">
                    <h2>PDRN : Matrice<br>Polynucléotidique</h2>
                    <p>
                        Le Polydésoxyribonucléotide (PDRN) est une chaîne de polymères d'ADN purifiée. Contrairement aux peptides de surface, le PDRN possède la capacité d'interagir directement avec le métabolisme cellulaire grâce à son homologie de 97% avec le génome humain, éliminant ainsi toute réponse immunogène.
                    </p>
                    <p>
                        Son activité pharmacologique principale réside dans sa liaison sélective aux récepteurs A2A de l'adénosine. Cette activation "salvage pathway" (voie de sauvetage) induit une prolifération fibroblastique majeure, une néoangiogenèse et une réduction de la sécrétion de cytokines inflammatoires.
                    </p>
                    <p>
                        Concentré à 1% (grade clinique), le sérum Luméra offre une dose topique maximale autorisée, conçue pour être acheminée dans le derme via la micro-induction (CIT).
                    </p>
                    <div class="pdrn-data-row">
                        <div class="pdrn-data-box">
                            <span class="value">A2A</span>
                            <span class="label">Récepteur Purinergique<br>Ciblé</span>
                        </div>
                        <div class="pdrn-data-box">
                            <span class="value">97%</span>
                            <span class="label">Taux d'Homologie<br>Génomique</span>
                        </div>
                        <div class="pdrn-data-box">
                            <span class="value">10k</span>
                            <span class="label">Poids Moléculaire<br>(Daltons)</span>
                        </div>
                        <div class="pdrn-data-box">
                            <span class="value">1.0%</span>
                            <span class="label">Concentration<br>Clinique Active</span>
                        </div>
                    </div>
                </div>
                <div class="pdrn-mechanism reveal-right">
                    <h4 style="font-family:var(--font-sans);font-size:0.72rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:var(--c-text-lighter);margin-bottom:1.5rem;">Cascade Pharmacodynamique</h4>
                    <div class="mech-step">
                        <div class="mech-step-num">·</div>
                        <div class="mech-step-body">
                            <h4>Affinité Réceptoriale</h4>
                            <p>Liaison de haute affinité aux récepteurs A2A des fibroblastes dermiques.</p>
                        </div>
                    </div>
                    <div class="mech-step">
                        <div class="mech-step-num">·</div>
                        <div class="mech-step-body">
                            <h4>Signalisation Intracellulaire</h4>
                            <p>Élévation de l'AMPc intracellulaire activant les voies de prolifération.</p>
                        </div>
                    </div>
                    <div class="mech-step">
                        <div class="mech-step-num">·</div>
                        <div class="mech-step-body">
                            <h4>Régulation Matricielle</h4>
                            <p>Synthèse de novo de collagène de type I et d'acide hyaluronique endogène.</p>
                        </div>
                    </div>
                    <div class="mech-step">
                        <div class="mech-step-num">·</div>
                        <div class="mech-step-body">
                            <h4>Anti-inflammation</h4>
                            <p>Inhibition de l'interleukine-6 (IL-6) et du TNF-α (réponse apaisante tissulaire).</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ PDRN ═══ -->', '<!-- ═══ CIT · MICRONEEDLING ═══ -->', pdrn_new)

# 7. CIT
cit_new = """    <section class="cit-section">
        <div class="container">
            <div class="section-eyebrow">Vecteur 03</div>
            <div class="cit-split">
                <div class="cit-info reveal-left">
                    <h2>CIT : Induction Tissulaire<br>Contrôlée</h2>
                    <p>
                        La Collagen Induction Therapy (CIT) exploite la réponse physiologique de cicatrisation cutanée. Le passage du stylo crée un réseau de micro-perforations calibrées qui agissent comme un signal de détresse cellulaire, initiant instantanément la cascade de libération des facteurs de croissance.
                    </p>
                    <p>
                        La profondeur de 0,25 mm est un standard de sécurité strict pour l'usage non-médical. Elle garantit l'atteinte de la jonction dermo-épidermique sans risquer la fibrose ni l'effraction vasculaire majeure. Cette profondeur maximise la perméabilité de la couche cornée, augmentant la biodisponibilité transcutanée du sérum de près de 470%.
                    </p>
                    <div class="cit-signals">
                        <div class="signal-chip">
                            <strong>PDGF</strong>
                            Platelet-Derived Growth Factor — Chimiotaxie des fibroblastes
                        </div>
                        <div class="signal-chip">
                            <strong>TGF-β</strong>
                            Transforming Growth Factor — Synthèse de matrice extracellulaire
                        </div>
                        <div class="signal-chip">
                            <strong>VEGF</strong>
                            Vascular Endothelial Growth Factor — Néovascularisation
                        </div>
                        <div class="signal-chip">
                            <strong>EGF</strong>
                            Epidermal Growth Factor — Réépithélialisation tissulaire
                        </div>
                    </div>
                </div>
                <div class="cit-visual reveal-right">
                    <div class="cit-depth-chart">
                        <h4>Calibration Pénétrative</h4>

                        <div class="depth-hero">
                            <div class="depth-hero-mm">0,25<span>mm</span></div>
                            <div class="depth-hero-body">
                                <span class="depth-hero-badge">Norme CEE Usage Domicile</span>
                                <p>Cible le stratum corneum et l'épiderme basal. Pénétration sécurisée, sans anesthésie topique requise.</p>
                            </div>
                        </div>

                        <ul class="depth-scale">
                            <li class="depth-step is-safe">
                                <span class="depth-step-mm">0,30 mm</span>
                                <span class="depth-track"><span class="depth-fill" style="--d:.20"></span></span>
                                <span class="depth-step-tag">Sécurité Domicile</span>
                            </li>
                            <li class="depth-step is-pro">
                                <span class="depth-step-mm">1,00 mm</span>
                                <span class="depth-track"><span class="depth-fill" style="--d:.70"></span></span>
                                <span class="depth-step-tag">Usage Professionnel</span>
                            </li>
                            <li class="depth-step is-medical">
                                <span class="depth-step-mm">1,50+ mm</span>
                                <span class="depth-track"><span class="depth-fill" style="--d:1"></span></span>
                                <span class="depth-step-tag">Acte Médical</span>
                            </li>
                        </ul>
                    </div>
                    <div class="cit-synergy-callout">
                        <h4>Fenêtre Thérapeutique : 60 minutes</h4>
                        <p>Les micro-canaux épidermiques subissent une fermeture physiologique en 60 à 90 minutes. L'administration topique du complexe PDRN doit impérativement intervenir dans ce délai pour contourner la barrière lipophile épidermique.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ CIT · MICRONEEDLING ═══ -->', '<!-- ═══ ÉTUDES CLINIQUES ═══ -->', cit_new)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
