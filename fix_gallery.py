import glob, re

js_block = """        document.querySelectorAll('.gallery-stage').forEach(function(stage){
          var main=stage.querySelector('.gallery-carousel');
          if(!main)return;
          var gallery=stage.closest('.product-gallery')||stage.parentNode;
          var thumbsWrap=gallery.querySelector('.gallery-thumbs');
          var ts=thumbsWrap?Array.prototype.slice.call(thumbsWrap.querySelectorAll('img')):[];
          var prev=stage.querySelector('.gallery-arrow.prev'),next=stage.querySelector('.gallery-arrow.next');
          var count=main.querySelectorAll('img').length;
          
          var pagination = document.createElement('div');
          pagination.className = 'gallery-pagination';
          var dots = [];
          for (var k = 0; k < count; k++) {
              var dot = document.createElement('div');
              dot.className = 'gallery-dot';
              (function(idx) { dot.addEventListener('click', function() { go(idx); }); })(k);
              pagination.appendChild(dot);
              dots.push(dot);
          }
          gallery.appendChild(pagination);

          main.scrollLeft=0;
          window.addEventListener('load',function(){main.scrollLeft=0;sync();});
          function current(){return Math.round(main.scrollLeft/main.clientWidth);}
          function go(i){i=Math.max(0,Math.min(count-1,i));main.scrollTo({left:main.clientWidth*i,behavior:'smooth'});}
          ts.forEach(function(t,i){t.addEventListener('click',function(){go(i);});});
          if(prev)prev.addEventListener('click',function(){go(current()-1);});
          if(next)next.addEventListener('click',function(){go(current()+1);});
          function sync(){
            var i=current();
            ts.forEach(function(t,j){t.classList.toggle('active',j===i);});
            dots.forEach(function(d,j){d.classList.toggle('active',j===i);});
            if(prev)prev.disabled=i<=0;
            if(next)next.disabled=i>=count-1;
            var act=ts[i];if(act&&thumbsWrap)thumbsWrap.scrollTo({left:act.offsetLeft-(thumbsWrap.clientWidth-act.clientWidth)/2,behavior:'smooth'});
          }
          var raf;
          main.addEventListener('scroll',function(){if(raf)return;raf=requestAnimationFrame(function(){sync();raf=null;});},{passive:true});
          sync();
        });"""

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to match the old block
    # Start: document.querySelectorAll('.gallery-stage').forEach(function(stage){
    # End: });\n      })();
    pattern = r"document\.querySelectorAll\('\.gallery-stage'\)\.forEach\(function\(stage\)\{[\s\S]*?sync\(\);\s*\}\);"
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, js_block.strip(), content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated", file)
