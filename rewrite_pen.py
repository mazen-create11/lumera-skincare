import re

with open('product-pen.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n            ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

new_acc = """    <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Induction Tissulaire (CIT)<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">Le microneedling agit par effraction mécanique de la couche cornée, générant un stress tissulaire contrôlé.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Cascade Cicatricielle :</strong> Libération autocrine de facteurs de croissance (PDGF, TGF-β, VEGF).</li>
                                <li><strong>✦ Calibration 0,25mm :</strong> Profondeur optimisée pour l'usage non-médical. N'induit aucune lésion vasculaire majeure.</li>
                                <li><strong>✦ Biodisponibilité :</strong> Multiplie par 4.7 la pénétration du sérum PDRN dans le derme superficiel.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Protocole Sanitaire & Usage<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Asepsie :</strong> Désinfection intégrale de l'embout à l'alcool à 70° avant et après chaque séance.</li>
                                <li><strong>✦ Cinétique :</strong> Application en quadrillage doux (vertical, horizontal, diagonal). Ne jamais exercer de pression forte.</li>
                                <li><strong>✦ Fréquence :</strong> 1 séance par semaine (phase active) ou 1 séance toutes les 2 semaines (phase d'entretien).</li>
                                <li><strong>✦ Remplacement :</strong> La cartouche d'aiguilles doit être changée tous les 1 à 2 mois pour garantir l'intégrité de la perforation.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">Contre-indications Strictes<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Interdictions :</strong> Ne jamais utiliser sur acné active, rosacée inflammatoire, eczéma ou plaies ouvertes.</li>
                                <li><strong>✦ Incompatibilités Topiques :</strong> Ne pas appliquer de Rétinol, AHA/BHA, ou Vitamine C pure dans les 24h suivant la séance.</li>
                                <li><strong>✦ Photoprotection :</strong> Éviter l'exposition solaire directe pendant 48h. Un écran total SPF50+ est obligatoire.</li>
                            </ul>
                        </div>
                    </div>
                </div>"""

html = replace_section(html, '<!-- Accordions -->\n            <div class="accordion reveal">', '</div>\n        </div>', new_acc)

with open('product-pen.html', 'w', encoding='utf-8') as f:
    f.write(html)
