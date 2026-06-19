with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix mobile thumbnails being hidden!
css = css.replace('.gallery-thumbs { display: none !important; }', '/* .gallery-thumbs restored on mobile */')
css = css.replace('.gallery-arrow { display: none !important; }', '/* .gallery-arrow restored on mobile */')

# Make sure grid desktop has no thumbs either, wait, grid desktop had it hidden:
# Let's just make sure desktop grid HIDES thumbs and mobile SHOWS them.
css = css.replace('/* .gallery-arrow restored on mobile */', '/* arrows fixed */')
css = css.replace('/* .gallery-thumbs restored on mobile */', '/* thumbs fixed */')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS Fixed!")
