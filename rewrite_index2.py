import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_section(html, start_marker, end_marker, new_content):
    pattern = re.compile(rf'({re.escape(start_marker)}).*?(?={re.escape(end_marker)})', re.DOTALL)
    if pattern.search(html):
        return pattern.sub(rf'\1\n{new_content}\n    ', html)
    else:
        print(f"Marker not found: {start_marker}")
        return html

why_new = """    <div class="container">
        <div class="why-grid">
            <div class="reveal">
                <span class="eyebrow">Ingénierie Biomédicale</span>
                <h2 class="h2">Le postulat<br><em>clinique.</em></h2>
                <div class="why-rows">
                    <div class="why-row">
                        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
                        <span>Homologie Génomique 97% (Sérum PDRN)</span>
                    </div>
                    <div class="why-row">
                        <div class="why-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div>
                        <span>Spectre Optique Calibré (630nm / 840nm)</span>
                    </div>
                    <div class="why-row">
                        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
                        <span>Induction Fibroblastique (Profondeur 0,25mm)</span>
                    </div>
                    <div class="why-row">
                        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
                        <span>Fabrication certifiée ISO 13485 (Grade Médical)</span>
                    </div>
                </div>
            </div>
            <div class="compare-wrap reveal-r">
                <div class="compare-row compare-head">
                    <div class="compare-feat">Étude Comparative</div>
                    <div class="compare-lum">Le protocole<br><strong>LUMÉRA</strong></div>
                    <div class="compare-other">Masques LED<br>Rigides</div>
                </div>
                <div class="compare-row">
                    <div class="compare-feat">Couverture dermique</div>
                    <div class="compare-lum">Visage + Cou (intégral)</div>
                    <div class="compare-other">Visage seul</div>
                </div>
                <div class="compare-row">
                    <div class="compare-feat">Distance Tissu-Source</div>
                    <div class="compare-lum">1 mm (Silicone Flexible)</div>
                    <div class="compare-other">> 15 mm</div>
                </div>
                <div class="compare-row">
                    <div class="compare-feat">Déperdition Optique</div>
                    <div class="compare-lum">Nulle (Contact Direct)</div>
                    <div class="compare-other">Dispersive (Loi carrée inverse)</div>
                </div>
                <div class="compare-row">
                    <div class="compare-feat">Biodisponibilité PDRN</div>
                    <div class="compare-lum">×4.7 (post-induction)</div>
                    <div class="compare-other">Topique (Limitée)</div>
                </div>
                <div class="compare-note">L'intensité lumineuse d'une source non-apposée diminue de façon quadratique avec la distance. Le silicone médical flexible Luméra garantit une irradation tissulaire totale.</div>
            </div>
        </div>
        
        <div class="statband reveal">
            <div class="statband-grid">
                <div class="c"><span class="v">1%</span><span class="l">PDRN Grade Clinique</span></div>
                <div class="c"><span class="v">10k</span><span class="l">Daltons Poids Moléculaire</span></div>
                <div class="c"><span class="v">630<span style="font-size:1.2rem;font-weight:400;color:var(--text-mid)">nm</span></span><span class="l">Longueur d'onde Rouge</span></div>
                <div class="c"><span class="v">840<span style="font-size:1.2rem;font-weight:400;color:var(--text-mid)">nm</span></span><span class="l">Longueur d'onde NIR</span></div>
            </div>
        </div>
    </div>"""
html = replace_section(html, '<!-- WHY -->\n<section class="sec why">', '<!-- FOUNDER -->', why_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
