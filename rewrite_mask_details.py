import re

with open('product-mask.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n                ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

new_acc_1 = """                <div class="acc-body">
                  <div class="acc-content">
                    <p style="font-size:0.92rem; line-height:1.7; color:var(--text-mid); margin-bottom:1.5rem">Le masque Luméra utilise un protocole de photobiomodulation (PBM) à double spectre pour cibler directement le métabolisme cellulaire.</p>
                    <ul class="acc-list">
                      <li><strong>✦ Synthèse d'ATP :</strong> La cytochrome c oxydase absorbe l'énergie lumineuse, accélérant le métabolisme fibroblastique.</li>
                      <li><strong>✦ Restauration Matricielle :</strong> Augmentation documentée de la synthèse de collagène de type I et d'élastine.</li>
                      <li><strong>✦ Oxygénation Tissulaire :</strong> Micro-circulation améliorée via la libération d'oxyde nitrique (NO).</li>
                      <li><strong>✦ Indication :</strong> Rides structurelles, perte d'élasticité, teint terne, inflammation subaiguë.</li>
                    </ul>
                  </div>
                </div>"""

# Replace the "Indications Cliniques" (was Les bienfaits)
html = replace_section(html, '<button class="acc-btn">Indications Cliniques<span class="acc-ic">+</span></button>', '</div>', new_acc_1)

new_acc_2 = """                <div class="acc-body">
                  <div class="acc-content">
                    <ul class="acc-list">
                      <li><strong>✦ Étape 1 :</strong> Sur peau propre et sèche (ou après l'application du sérum PDRN dans le cadre du Rituel).</li>
                      <li><strong>✦ Étape 2 :</strong> Appliquez le masque en ajustant les sangles arrière. Le silicone médical doit épouser les contours de votre visage.</li>
                      <li><strong>✦ Étape 3 :</strong> Lancez le protocole (10 à 20 minutes). L'appareil s'éteint automatiquement.</li>
                      <li><strong>✦ Étape 4 :</strong> Fréquence recommandée : 3 à 5 séances par semaine pour une accumulation thérapeutique optimale.</li>
                    </ul>
                  </div>
                </div>"""
html = replace_section(html, '<button class="acc-btn">Protocole d\'Application<span class="acc-ic">+</span></button>', '</div>', new_acc_2)

new_acc_3 = """                <div class="acc-body">
                  <div class="acc-content">
                    <ul class="acc-list">
                      <li><strong>✦ Spectre Optique :</strong> Rouge Visible (630nm) & Proche Infrarouge (840nm)</li>
                      <li><strong>✦ Matériau :</strong> Élastomère de silicone de grade biomédical (FDA/CE)</li>
                      <li><strong>✦ Couverture :</strong> Architecture intégrale Visage + Cou</li>
                      <li><strong>✦ Certification :</strong> Conforme aux directives européennes (marquage CE), fabrication ISO 13485</li>
                      <li><strong>✦ Batterie :</strong> Lithium-ion rechargeable (autonomie : 8 à 10 cycles)</li>
                    </ul>
                  </div>
                </div>"""
html = replace_section(html, '<button class="acc-btn">Caractéristiques Techniques<span class="acc-ic">+</span></button>', '</div>', new_acc_3)

with open('product-mask.html', 'w', encoding='utf-8') as f:
    f.write(html)
