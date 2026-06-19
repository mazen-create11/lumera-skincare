import re

with open('product-serum.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n            ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

new_acc = """    <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Pharmacodynamie : PDRN 1%<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">Le Polydésoxyribonucléotide (PDRN) est un agoniste sélectif des récepteurs A2A purinergiques. Son homologie génomique (97%) annule la réponse immunogène et maximise la pénétration cellulaire.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Angiogenèse :</strong> Stimule la sécrétion de VEGF (Vascular Endothelial Growth Factor).</li>
                                <li><strong>✦ Prolifération :</strong> Augmentation in vitro de la synthèse collagénique par les fibroblastes dermiques.</li>
                                <li><strong>✦ Concentration :</strong> Formulé à 1% — dose maximale d'efficacité clinique topique.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Adjuvants Thérapeutiques<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">La formulation intègre des modélateurs synergiques pour optimiser l'environnement extra-cellulaire.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Niacinamide (5%) :</strong> Inhibe le transfert des mélanosomes. Consolidation de la fonction barrière.</li>
                                <li><strong>✦ Complexe Peptidique :</strong> Peptides biomimétiques agissant sur les récepteurs transmembranaires.</li>
                                <li><strong>✦ Acide Hyaluronique :</strong> Fractionné à triple poids moléculaire pour hydratation multi-stridale.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Protocole Séquencé<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Séquence 1 (Induction) :</strong> Après utilisation du stylo CIT 0,25mm pour bypasser la couche cornée.</li>
                                <li><strong>✦ Séquence 2 (Infusion) :</strong> Application immédiate du sérum. Absorption tissulaire multipliée.</li>
                                <li><strong>✦ Séquence 3 (Photomodulation) :</strong> Irradiation LED pour activer l'ATP et soutenir le métabolisme fibroblastique induit par le PDRN.</li>
                            </ul>
                        </div>
                    </div>
                </div>"""

html = replace_section(html, '<!-- Accordions -->\n            <div class="accordion reveal">', '</div>\n        </div>', new_acc)

with open('product-serum.html', 'w', encoding='utf-8') as f:
    f.write(html)
