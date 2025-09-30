import easyocr
from pathlib import Path

reader = easyocr.Reader(['en'])

def extract_text(image_path, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    results = reader.readtext(image_path, detail=0)
    text = "\n".join(results)
    (out_dir / "ocr_output.txt").write_text(text, encoding="utf-8")
    return text
