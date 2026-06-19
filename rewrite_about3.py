import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    return pattern.sub(rf'\1\n{new_content}\n    ', html)

# 8. ETUDES CLINIQUES
etudes_new = """    <section class="studies-section reveal">
        <div class="container">
            <div style="text-align:center;max-width:640px;margin:0 auto;">
                <div class="section-eyebrow">Littérature Médicale</div>
                <h2 class="section-title">Revue des données cliniques</h2>
                <p class="section-subtitle">Aperçu des publications indépendantes documentant l'efficacité des technologies intégrées (PBM, PDRN, CIT) in vivo et in vitro.</p>
            </div>
            <div class="studies-grid">
                <div class="study-card">
                    <span class="study-tag">Méta-analyse · PBM 630nm</span>
                    <h4>Évaluation de l'efficacité sur le vieillissement structurel</h4>
                    <p>Revue systématique de 22 études contrôlées randomisées évaluant la LED 630nm. Cohorte globale : 1 847 sujets. Durée de suivi : 8 à 24 semaines.</p>
                    <div class="study-result">
                        <span class="study-result-value">−36%</span>
                        <span class="study-result-detail">Indice de sévérité<br>des rides (J+84)</span>
                    </div>
                    <div class="study-source">Lee et al., 2023 — PMID: 37128566</div>
                </div>
                <div class="study-card">
                    <span class="study-tag">Essai Clinique · PBM 830nm</span>
                    <h4>Amélioration biomécanique de l'élasticité</h4>
                    <p>Étude prospective, randomisée en double aveugle. Évaluation de l'impact du proche infrarouge (NIR) sur l'élasticité cutanée mesurée par cutomètre (n=84).</p>
                    <div class="study-result">
                        <span class="study-result-value">+19%</span>
                        <span class="study-result-detail">Index d'élasticité<br>cutanée (J+56)</span>
                    </div>
                    <div class="study-source">Couturaud V., 2023 — Revue Française de Dermatologie</div>
                </div>
                <div class="study-card">
                    <span class="study-tag">Essai Clinique · Acné & LED</span>
                    <h4>Réduction du grade inflammatoire acnéique</h4>
                    <p>Étude contrôlée sur 86 sujets présentant une acné légère à modérée (grade I-II). Utilisation de LED bleues 470nm, bi-quotidiennement sur 12 semaines.</p>
                    <div class="study-result">
                        <span class="study-result-value">−53%</span>
                        <span class="study-result-detail">Comptage lésionnel<br>inflammatoire (J+84)</span>
                    </div>
                    <div class="study-source">J. Clin. Aesthet. Dermatol., 2021</div>
                </div>
                <div class="study-card">
                    <span class="study-tag">In Vitro · PDRN 1%</span>
                    <h4>Activation de la transcription collagénique</h4>
                    <p>Étude sur cultures de fibroblastes primaires humains (HDFs). Mesure de l'expression de l'ARNm du collagène de type I après exposition au PDRN.</p>
                    <div class="study-result">
                        <span class="study-result-value">+47%</span>
                        <span class="study-result-detail">Sécrétion protéique<br>vs. groupe contrôle (72h)</span>
                    </div>
                    <div class="study-source">Veronesi et al., 2021 — Int. J. Mol. Sci.</div>
                </div>
                <div class="study-card">
                    <span class="study-tag">Ex Vivo · Microneedling</span>
                    <h4>Analyse histologique post-induction</h4>
                    <p>Biopsies cutanées après protocole CIT à 0,25 mm. Coloration histochimique (Van Gieson) pour quantifier la néosynthèse de la matrice conjonctive.</p>
                    <div class="study-result">
                        <span class="study-result-value">+206%</span>
                        <span class="study-result-detail">Densité collagène I/III<br>mesurée à 8 semaines</span>
                    </div>
                    <div class="study-source">Aust et al., 2008 — Dermatologic Surgery</div>
                </div>
                <div class="study-card">
                    <span class="study-tag">Pharmacocinétique · CIT</span>
                    <h4>Perméabilité transépidermique</h4>
                    <p>Évaluation fluorométrique in vivo de la pénétration de macromolécules topiques appliquées 30 minutes après induction de micro-canaux épidermiques.</p>
                    <div class="study-result">
                        <span class="study-result-value">×4.7</span>
                        <span class="study-result-detail">Ratio d'absorption<br>post-CIT vs épiderme intact</span>
                    </div>
                    <div class="study-source">Badran et al., 2009 — Eur. J. Pharm. Biopharm.</div>
                </div>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ ÉTUDES CLINIQUES ═══ -->', '<!-- ═══ SYNERGIE ═══ -->', etudes_new)

# 9. SYNERGIE
synergie_new = """    <section class="synergy-section">
        <div class="container">
            <div class="section-eyebrow">Le Protocole Intégré</div>
            <h2 class="section-title">Ingénierie de la Synergie</h2>
            <p class="section-subtitle">Chaque modalité thérapeutique amplifie la biodisponibilité ou l'activité métabolique de la suivante, formant un continuum régénératif.</p>
            <div class="synergy-triangle">
                <div class="syn-node">
                    <div class="syn-icon" style="background:transparent; border:1px solid rgba(255,255,255,0.2); font-family:var(--font-serif); font-size:1.8rem; font-style:italic;">I</div>
                    <h3>Induction → Infusion</h3>
                    <p>L'effraction mécanique de la couche cornée par le stylo lève la barrière lipophile épidermique. Les macromolécules d'ADN du PDRN bénéficient d'un accès direct au derme papillaire via les micro-canaux de 0,25mm.</p>
                </div>
                <div class="syn-node">
                    <div class="syn-icon" style="background:transparent; border:1px solid rgba(255,255,255,0.2); font-family:var(--font-serif); font-size:1.8rem; font-style:italic;">II</div>
                    <h3>Infusion → Activation</h3>
                    <p>Le PDRN se fixe sur les récepteurs A2A fibroblastiques, déclenchant le signal de synthèse protéique. Ce processus extrêmement gourmand en énergie cellulaire est rendu possible par l'apport immédiat de l'étape suivante.</p>
                </div>
                <div class="syn-node">
                    <div class="syn-icon" style="background:transparent; border:1px solid rgba(255,255,255,0.2); font-family:var(--font-serif); font-size:1.8rem; font-style:italic;">III</div>
                    <h3>Activation → Photomodulation</h3>
                    <p>L'irradiation LED inonde la cellule d'ATP mitochondrial. Cette énergie alimente le métabolisme fibroblastique (activé par le PDRN) tout en modulant l'inflammation résiduelle générée par l'induction mécanique (CIT).</p>
                </div>
            </div>
            <div class="synergy-connection">
                <h4>Séquençage Chronologique du Rituel</h4>
                <p>
                    <strong style="color:var(--c-accent-light);">T0 ·</strong> Induction (5 min) : Création des canaux transépidermiques.
                    <br><strong style="color:var(--c-accent-light);">T+5 ·</strong> Infusion (Immédial) : Saturation des récepteurs A2A par le sérum PDRN 1%.
                    <br><strong style="color:var(--c-accent-light);">T+10 ·</strong> Photomodulation (20 min) : Amplification ATP et résolution inflammatoire par NIR.
                    <br><br>Ce protocole séquencé maximise l'efficience de chaque technologie. Une architecture thérapeutique digne d'un protocole clinique, appliquée au domicile.
                </p>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ SYNERGIE ═══ -->', '<!-- ═══ QUALITÉ & CERTIFICATIONS ═══ -->', synergie_new)

# 10. QUALITE & CERTIFICATIONS + MANIFESTE
qualite_new = """    <section class="quality-section reveal">
        <div class="container">
            <div style="text-align:center;max-width:640px;margin:0 auto 0;">
                <div class="section-eyebrow">Conformité Réglementaire</div>
                <h2 class="section-title">Standards Normatifs</h2>
                <p class="section-subtitle">Une ingénierie suisse et européenne, régie par les normes les plus strictes de la sécurité des dispositifs médicaux.</p>
            </div>
            <div class="quality-grid">
                <div class="quality-card">
                    <div class="quality-icon" style="border:none; background:transparent; font-size:1.6rem; color:var(--c-text);">✦</div>
                    <h4>Directives CEE</h4>
                    <p>Conformité intégrale aux directives européennes LVD 2014/35/UE et CEM 2014/30/UE sur la compatibilité électromagnétique.</p>
                </div>
                <div class="quality-card">
                    <div class="quality-icon" style="border:none; background:transparent; font-size:1.6rem; color:var(--c-text);">✦</div>
                    <h4>Grade Biomédical</h4>
                    <p>Utilisation exclusive d'élastomère de silicone de grade médical, garantissant une innocuité dermatologique totale.</p>
                </div>
                <div class="quality-card">
                    <div class="quality-icon" style="border:none; background:transparent; font-size:1.6rem; color:var(--c-text);">✦</div>
                    <h4>Norme ISO 13485</h4>
                    <p>Fabrication certifiée selon le standard international des systèmes de management de la qualité pour dispositifs médicaux.</p>
                </div>
                <div class="quality-card">
                    <div class="quality-icon" style="border:none; background:transparent; font-size:1.6rem; color:var(--c-text);">✦</div>
                    <h4>Formulation Haute Tolérance</h4>
                    <p>Sérum formulé sans perturbateurs endocriniens, phtalates, parabènes ni parfums synthétiques. Compatibilité clinique maximale.</p>
                </div>
            </div>
            <div class="cert-strip">
                <div class="cert-item">
                    <div class="cert-badge-lg">CE</div>
                    <span>Directives UE</span>
                </div>
                <div class="cert-item">
                    <div class="cert-badge-lg">ISO</div>
                    <span>ISO 13485</span>
                </div>
                <div class="cert-item">
                    <div class="cert-badge-lg" style="font-size:0.75rem;">RG0</div>
                    <span>Sécurité Oculaire</span>
                </div>
                <div class="cert-item">
                    <div class="cert-badge-lg" style="font-size:0.75rem;">RoHS</div>
                    <span>Conformité Matériaux</span>
                </div>
                <div class="cert-item">
                    <div class="cert-badge-lg" style="font-size:0.7rem;">DERMA</div>
                    <span>Tolérance Clinique</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ═══ MANIFESTE ═══ -->
    <section class="manifesto-section reveal">
        <div class="container">
            <blockquote>
                "La médecine régénérative n'est plus confinée à la clinique.<br>
                <em>C'est le nouveau paradigme de la dermo-cosmétique.</em>"
            </blockquote>
            <div class="manifesto-meta">
                <div class="manifesto-divider"></div>
                <span>Département Recherche & Développement · Luméra</span>
            </div>
        </div>
    </section>"""
html = replace_section(html, '<!-- ═══ QUALITÉ & CERTIFICATIONS ═══ -->', '<!-- ═══ CTA FINAL ═══ -->', qualite_new)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
