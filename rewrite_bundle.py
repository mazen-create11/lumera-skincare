import re

with open('bundle.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n            ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

new_acc = """    <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">1. L'Induction (CIT 0,25mm)<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">La première phase du rituel consiste à bypasser la barrière cutanée.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Mécanisme :</strong> Le stylo crée des micro-canaux épidermiques, déclenchant un signal autocrine de réparation (facteurs de croissance).</li>
                                <li><strong>✦ Résultat :</strong> L'absorption des actifs appliqués par la suite est multipliée par 4.7.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">2. L'Infusion (Sérum PDRN 1%)<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">Application immédiate des bio-macromolécules dans la fenêtre thérapeutique de 60 minutes.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Mécanisme :</strong> Le PDRN (Polydésoxyribonucléotide) s'infiltre dans le derme papillaire via les micro-canaux et active les récepteurs A2A fibroblastiques.</li>
                                <li><strong>✦ Résultat :</strong> Initiation massive de la synthèse d'acide hyaluronique et de collagène de type I.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header" aria-expanded="false">3. La Photomodulation (Masque LED)<span class="icon">+</span></button>
                    <div class="accordion-content">
                        <div style="padding-bottom:1.5rem; font-size:0.92rem; color:var(--text-mid); line-height:1.7;">
                            <p style="margin-bottom:1rem">L'étape finale fournit l'énergie nécessaire à la transcription cellulaire.</p>
                            <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.6rem;">
                                <li><strong>✦ Mécanisme :</strong> L'irradiation (630nm / 840nm) stimule la cytochrome C oxydase. Le métabolisme cellulaire, déjà sollicité par le PDRN, est inondé d'ATP.</li>
                                <li><strong>✦ Résultat :</strong> La régénération cellulaire est accélérée, l'inflammation induite par le microneedling est résolue, et la peau est structurellement densifiée.</li>
                            </ul>
                        </div>
                    </div>
                </div>"""

html = replace_section(html, '<!-- Accordions -->\n            <div class="accordion reveal">', '</div>\n        </div>', new_acc)

with open('bundle.html', 'w', encoding='utf-8') as f:
    f.write(html)
