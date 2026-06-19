import glob

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('href="styles.css?v=5"', 'href="styles.css?v=6"')
    content = content.replace('href="styles.css"', 'href="styles.css?v=6"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

