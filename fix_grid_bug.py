with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Disable scroll snapping on the desktop grid layout
css = css.replace("grid-template-columns: 1fr 1fr;", "grid-template-columns: 1fr 1fr;\n        scroll-snap-type: none !important;")
css = css.replace("aspect-ratio: 1/1 !important; /* Format carré parfait */", "aspect-ratio: 1/1 !important;\n        scroll-snap-align: none !important;")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Grid snap bug fixed")
