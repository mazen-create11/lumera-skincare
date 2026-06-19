import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add Custom Scrollbar
scrollbar_css = """
/* CUSTOM SCROLLBAR */
::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-track { background: var(--cream); }
::-webkit-scrollbar-thumb { background: #E0CDD2; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: var(--rose-dark); }
"""
if "::-webkit-scrollbar {" not in css:
    css = css.replace("/* BUTTONS */", scrollbar_css + "\n/* BUTTONS */")

# 2. Performance: content-visibility
perf_css = """
/* PERFORMANCE OPTS */
.reviews, .faq, .features, .section-ingredients { content-visibility: auto; contain-intrinsic-size: auto 800px; }
"""
if "content-visibility:" not in css:
    css += "\n" + perf_css

# 3. Smooth Hover & Animations (Scroll reveal)
anim_css = """
/* SCROLL REVEAL ANIMATIONS */
.reveal-up {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1), transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}
.reveal-up.is-visible {
    opacity: 1;
    transform: translateY(0);
}
"""
if ".reveal-up {" not in css:
    css += "\n" + anim_css

# 4. SATC animation refinement
css = css.replace(".satc { position: fixed; bottom: -100px;", ".satc { position: fixed; bottom: -100px; transition: bottom 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.4s;")
css = css.replace(".satc.show { bottom: 0;", ".satc.show { bottom: 0; opacity: 1;")
css = css.replace(".satc {", ".satc { opacity: 0;")

# 5. Hover media query wrapping for cards and buttons
# We need to ensure hover effects only apply on devices that support hover.
# This is tricky with regex, so we'll do it manually for the most important ones.
css = css.replace(".pcard:hover,.step:hover,.fcard:hover{", "@media(hover: hover){ .pcard:hover,.step:hover,.fcard:hover{")
css = css.replace("border-color:var(--rose)}", "border-color:var(--rose)} }")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("styles.css updated")
