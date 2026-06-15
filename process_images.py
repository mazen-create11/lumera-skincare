import os
from PIL import Image, ImageChops

def trim_black_borders(im):
    # Convert to RGB to ensure (0,0,0) is purely black
    bg = Image.new(im.mode, im.size, (0,0,0))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        # Only crop if there's significant black border
        return im.crop(bbox)
    return im

src_dir = "/Users/chabanmazen/.gemini/antigravity/brain/5e0f341e-f866-44cf-8962-5d6662806e4d/"
dest_dir = "/Users/chabanmazen/.gemini/antigravity/scratch/lumera-skincare/assets/"

for f in os.listdir(src_dir):
    if f.endswith((".png", ".jpg")):
        try:
            im = Image.open(os.path.join(src_dir, f)).convert("RGB")
            trimmed = trim_black_borders(im)
            w, h = trimmed.size
            
            # The side-by-side collages uploaded (e.g. 834x1024, 962x1024)
            # or the UGC ones (some are side-by-side)
            if w >= h * 0.9 and w > 600:
                # It's likely a side-by-side collage, split it vertically
                left = trimmed.crop((0, 0, w//2, h))
                right = trimmed.crop((w//2, 0, w, h))
                left.save(os.path.join(dest_dir, f"split_L_{f.split('.')[0]}.jpg"), quality=95)
                right.save(os.path.join(dest_dir, f"split_R_{f.split('.')[0]}.jpg"), quality=95)
                print(f"Split {f} into L/R ({w}x{h})")
            else:
                trimmed.save(os.path.join(dest_dir, f"crop_{f.split('.')[0]}.jpg"), quality=95)
                print(f"Cropped {f} to ({w}x{h})")
        except Exception as e:
            print(f"Error processing {f}: {e}")
