"""
Remplace le fond d'une photo produit en gardant le produit IDENTIQUE.
Utilise rembg pour créer le masque, puis OpenAI images.edit avec ce masque.
"""
import sys, os, io, json, base64
from pathlib import Path

# Clé API
API_KEY = "PLACEHOLDER"  # injectée depuis .claude.json

from rembg import remove
from PIL import Image
import urllib.request, urllib.parse

def load_api_key():
    claude_json = Path.home() / ".claude.json"
    d = json.loads(claude_json.read_text())
    proj = d["projects"]["/Users/chabanmazen"]
    return proj["mcpServers"]["openai-images"]["env"]["OPENAI_API_KEY"]

def make_mask(input_path: str) -> bytes:
    """Retourne un PNG RGBA : product=opaque(255), background=transparent(0)."""
    img = Image.open(input_path).convert("RGBA")
    removed = remove(img)  # RGBA, background transparent
    # Crée masque : noir opaque là où le produit est, transparent ailleurs
    mask = Image.new("RGBA", img.size, (0, 0, 0, 0))
    pixels = list(removed.getdata())
    mask_pixels = [(0, 0, 0, 255) if p[3] > 10 else (0, 0, 0, 0) for p in pixels]
    mask.putdata(mask_pixels)
    buf = io.BytesIO()
    mask.save(buf, format="PNG")
    return buf.getvalue()

def make_rgba_png(input_path: str) -> bytes:
    img = Image.open(input_path).convert("RGBA")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def edit_image_with_mask(api_key: str, image_bytes: bytes, mask_bytes: bytes, prompt: str, output_path: str, size="1024x1024"):
    import requests
    resp = requests.post(
        "https://api.openai.com/v1/images/edits",
        headers={"Authorization": f"Bearer {api_key}"},
        files={
            "image": ("image.png", image_bytes, "image/png"),
            "mask": ("mask.png", mask_bytes, "image/png"),
        },
        data={
            "model": "gpt-image-1",
            "prompt": prompt,
            "size": size,
            "n": "1",
            "quality": "high",
        },
        timeout=180,
    )
    if resp.status_code != 200:
        print(f"Erreur API: {resp.status_code} {resp.text[:300]}")
        return False
    result = resp.json()
    img_data = base64.b64decode(result["data"][0]["b64_json"])
    Path(output_path).write_bytes(img_data)
    print(f"Saved: {output_path}")
    return True

if __name__ == "__main__":
    api_key = load_api_key()
    input_img = sys.argv[1]
    output_img = sys.argv[2]
    prompt = sys.argv[3]

    print("Generating mask with rembg...")
    image_bytes = make_rgba_png(input_img)
    mask_bytes = make_mask(input_img)

    # Save mask for debug
    Path("/tmp/lumera_mask_debug.png").write_bytes(mask_bytes)
    print("Mask saved to /tmp/lumera_mask_debug.png")

    print("Calling OpenAI images.edit...")
    edit_image_with_mask(api_key, image_bytes, mask_bytes, prompt, output_img)
