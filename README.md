# VLM Image Explainer (BLIP-based)

🧠 Minimal demo that uses an open-source Vision-Language Model (BLIP) to generate natural-language explanations of images. Built for learning and demonstration: simple Streamlit frontend, small Python backend, CPU-friendly by default.

---

## Features ✅
- Simple Streamlit UI to upload an image (PNG/JPG) and request an explanation
- Uses existing `generate_explanation(image_path)` function (no model logic changes)
- Lazy model loading, clear error messages, and minimal UI

---

## Requirements
- Python 3.9+ recommended
- See `requirements.txt` (includes `torch`, `transformers`, `pillow`, `streamlit`, `accelerate`)

Quick install:

```bash
python -m venv .venv
.\.venv\Scripts\activate  # PowerShell/CMD on Windows
pip install -r requirements.txt
```

---

## Running
- Streamlit GUI (recommended):

```bash
streamlit run streamlit_app.py
```

- CLI preview (simple):

```bash
python app.py
```

The first model load may take time (downloads and initializes the model). On CPU this can be slow; please be patient.

---

## Configuration (env vars)
- `BLIP_MODEL` — override the Hugging Face model id or local model path. Default: `Salesforce/blip-image-captioning-base`.
- `HF_TOKEN` — optional Hugging Face token to access private models.

Set env vars in PowerShell (example):

```powershell
$env:BLIP_MODEL = "Salesforce/blip-image-captioning-base"
$env:HF_TOKEN = "<your_token_if_needed>"
```

Or run `huggingface-cli login` to configure long-lived credentials locally.

---

## Troubleshooting
- Error: "is not a local folder and is not a valid model identifier" — this usually means the model id is missing/invalid or the model is private.
  - Verify `BLIP_MODEL` is correct and public.
  - If private, set `HF_TOKEN` or run `huggingface-cli login`.
- If the app shows long waits, the model is probably downloading or initializing — allow several minutes on a slow CPU.
- To debug quickly, try running `python -c "from model import load_model; load_model()"` to surface model download/auth errors in the console.

---

## Notes & Tips
- The Streamlit UI saves an uploaded image to a temporary file and passes its path to `generate_explanation` to avoid changing your existing inference code.
- The project intentionally keeps the UI minimal and CPU-safe; no OCR, no external paid APIs.
- A `.gitignore` is included to avoid committing virtualenvs, caches, and secrets.

---

## Want improvements?
If you'd like, I can:
- Add a "Model status" check in the Streamlit UI to pre-load the model and show a status message.
- Add caching so repeated explanations for the same image are faster.
- Add more usage examples and a CONTRIBUTING section.

---

© 2026 — For learning/demo use only. No warranties.
