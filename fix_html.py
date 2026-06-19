import glob, re

js_reveal = """<script>
document.addEventListener("DOMContentLoaded", function() {
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal-up').forEach(function(el) {
    observer.observe(el);
  });
});
</script>
</body>"""

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add reveal-up class to section headers and cards
    content = content.replace('class="sec-title"', 'class="sec-title reveal-up"')
    content = content.replace('class="pcard"', 'class="pcard reveal-up"')
    content = content.replace('class="fcard"', 'class="fcard reveal-up"')
    
    # Add JS at the bottom
    if "IntersectionObserver" not in content and "reveal-up" in content:
        content = content.replace('</body>', js_reveal)
        
    # Index specific: fetchpriority="high"
    if file == "index.html":
        content = content.replace('src="assets/coffret-hero.webp?v=3"', 'src="assets/coffret-hero.webp?v=3" fetchpriority="high"')

    # Fix sticky-atc aria
    content = content.replace('class="satc-btn"', 'class="satc-btn" aria-label="Ajouter au panier"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        print("Updated", file)
