import re
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I want Desktop Grid to hide thumbs.
# I want Mobile to show thumbs.

# First, restore the desktop grid explicitly.
desktop_grid = """
    /* On cache la navigation mobile sur desktop */
    .gallery-arrow { display: none !important; }
    .gallery-thumbs { display: none !important; }
}
"""
if ".gallery-thumbs { display: none !important; }" not in css:
    css = css.replace('} /* Pagination Dots pour mobile */', desktop_grid + '\n/* Pagination Dots pour mobile */')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

