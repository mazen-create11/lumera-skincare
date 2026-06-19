import glob

emojis = ['✨', '💡', '🌿', '⚕️', '🇪🇺', '🔬', '🪡', '💧', '✅', '⭐', '👇']
for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        for e in emojis:
            if e in line:
                print(f"{file}:{i+1} : {line.strip()}")
                break

