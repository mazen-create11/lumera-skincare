import glob

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('href="styles.css?v=6"', 'href="styles.css?v=7"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

