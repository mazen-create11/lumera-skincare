import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def remove_section(html, start_marker, end_marker):
    pattern = re.compile(rf'{re.escape(start_marker)}.*?{re.escape(end_marker)}', re.DOTALL)
    return pattern.sub(end_marker, html)

# Remove the old COMPARATIF section since it's now integrated in WHY
html = remove_section(html, '<!-- COMPARATIF -->', '<!-- GARANTIE -->')

# Update the MANIFESTO / GARANTIE text to be more clinical
html = html.replace('<h2>La promesse<br><em>Luméra.</em></h2>', '<h2>Engagement<br><em>Clinique.</em></h2>')
html = html.replace('Un doute ? Essayez-le pendant 30 jours, chez vous.', 'Protocole validé. 30 jours d\'essai clinique à domicile.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
