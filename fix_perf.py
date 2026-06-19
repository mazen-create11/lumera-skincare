import glob

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Cache buster for CSS to ensure changes are visible
    content = content.replace('href="styles.css"', 'href="styles.css?v=5"')
    content = content.replace('href="styles.css?v=2"', 'href="styles.css?v=5"')
    content = content.replace('href="styles.css?v=3"', 'href="styles.css?v=5"')
    content = content.replace('href="styles.css?v=4"', 'href="styles.css?v=5"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Remove content-visibility from CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("content-visibility: auto; contain-intrinsic-size: auto 800px;", "/* removed content-visibility due to scroll bugs */")
css = css.replace("transition: bottom 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.4s;", "transition: bottom 0.3s ease-in-out, opacity 0.3s;")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Perf fixed and cache busted!")
