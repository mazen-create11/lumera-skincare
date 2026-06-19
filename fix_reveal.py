import glob

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

    # If the file doesn't have the reveal-up observer, add it
    if "is-visible" not in content and "reveal-up" in content:
        content = content.replace('</body>', js_reveal)
    
    # Also, make sure that .reveal elements work (if we changed them to .reveal-up)
    # The user complained about missing photos... 
    # the product info text uses class="reveal".
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed reveal script!")
