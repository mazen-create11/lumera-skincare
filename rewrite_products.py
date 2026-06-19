import re
import glob

def clinical_rewrite(text):
    # Replace any remaining basic phrases with clinical ones
    replacements = [
        ('✨', '✦'),
        ('💡', '✦'),
        ('🌿', '✦'),
        ('⚕️', '✦'),
        ('🔬', '✦'),
        ('👇', '✦'),
        ('⭐', '✦'),
        ('✅', '✦'),
        ('❤️', '✦'),
        ('💧', '✦'),
        ('🪡', '✦'),
        ('🇪🇺', '✦'),
        ('pourquoi luméra', 'Ingénierie Biomédicale'),
        ('Les bienfaits', 'Indications Cliniques'),
        ('Comment l\'utiliser', 'Protocole d\'Application'),
        ('Spécifications', 'Caractéristiques Techniques'),
        ('lumière rouge', 'photobiomodulation 630nm'),
        ('Infrarouge', 'Proche Infrarouge (NIR) 840nm'),
        ('réduit les rides', 'restaure la matrice conjonctive'),
        ('anti-âge', 'régénératif'),
        ('booster le collagène', 'synthèse de collagène de type I'),
        ('belle peau', 'intégrité épidermique'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

for file in glob.glob("product-*.html") + ["bundle.html"]:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = clinical_rewrite(html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Rewrote products.")
