import pytesseract
from PIL import Image

def extract_text(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"[ERROR] Gagal membaca gambar: {e}"
