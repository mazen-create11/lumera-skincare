import re

with open('product-mask.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n            ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

new_acc = """    <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Spectre Optique : Photobiomodulation<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">La photobiomodulation (PBM) ne chauffe pas les tissus, elle communique avec eux. Nos diodes émettent un rayonnement calibré pour être absorbé par la cytochrome c oxydase, l'enzyme clé de la respiration cellulaire.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Rouge Visible (630nm) :</strong> Pénétration épidermique. Rétablit l'uniformité du teint et stimule les kératinocytes superficiels.</li>
                                <li><strong>✦ Proche Infrarouge (840nm) :</strong> Pénétration dermique profonde (réticulaire). Induit la synthèse d'ATP et favorise la néocollagenèse.</li>
                                <li><strong>✦ Synergie :</strong> La combinaison des deux spectres permet une régulation globale de la matrice extra-cellulaire.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Ingénierie des Matériaux : Élastomère de Silicone<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">Les masques rigides conventionnels perdent jusqu'à 90% de l'intensité lumineuse selon la loi en carré inverse (dispersion optique). Le masque Luméra annule cette déperdition.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Biodisponibilité maximale :</strong> L'apposition directe sur la peau garantit qu'aucune énergie lumineuse ne se dissipe dans l'air.</li>
                                <li><strong>✦ Tolérance Clinique :</strong> Silicone de grade biomédical non-poreux, antibactérien et inerte chimiquement.</li>
                                <li><strong>✦ Couverture anatomique :</strong> Épouse chaque relief du visage et inclut le traitement spécifique du cou.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Protocole Thérapeutique<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Phase d'attaque :</strong> 3 à 5 séances hebdomadaires (10 min) pendant 12 semaines pour atteindre le seuil thérapeutique.</li>
                                <li><strong>✦ Phase d'entretien :</strong> 2 séances hebdomadaires suffisent à maintenir la sur-expression fibroblastique.</li>
                                <li><strong>✦ Séquençage :</strong> À utiliser impérativement sur peau sèche. L'intégration optimale s'effectue après l'application du sérum PDRN.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Conformité et Certification<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Directive Européenne :</strong> Marquage CE validant la conformité électromagnétique et photobiologique (Norme sécurité oculaire).</li>
                                <li><strong>✦ Ingénierie :</strong> Fabrication auditée selon la norme ISO 13485 (Dispositifs médicaux).</li>
                                <li><strong>✦ Conception :</strong> Design et contrôle qualité exclusifs au territoire français.</li>
                            </ul>
                        </div>
                    </div>
                </div>"""

html = replace_section(html, '<!-- Accordions -->\n            <div class="accordion reveal">', '</div>\n        </div>', new_acc)

with open('product-mask.html', 'w', encoding='utf-8') as f:
    f.write(html)
