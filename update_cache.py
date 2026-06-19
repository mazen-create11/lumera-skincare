import glob

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update cache buster
    content = content.replace('href="styles.css?v=7"', 'href="styles.css?v=8"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
