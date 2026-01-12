# inference.py

from PIL import Image
import torch
from model import load_model

# Lazy-loaded model and processor to avoid loading at import time
_model = None
_processor = None


def _get_model():
    global _model, _processor
    if _model is None or _processor is None:
        try:
            _model, _processor = load_model()
            _model.to(torch.device("cpu"))
        except Exception as e:
            raise RuntimeError(f"Error loading model: {e}") from e
    return _model, _processor


def generate_explanation(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")

    prompt = (
        "Explain what is happening in this image. "
        "If this looks like an error, UI issue, or chart, "
        "describe it clearly in simple terms."
    )

    model, processor = _get_model()

    inputs = processor(
        images=image,
        text=prompt,
        return_tensors="pt"
    )

    # Ensure tensors are on CPU
    inputs = {k: v.to(torch.device("cpu")) for k, v in inputs.items()}

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=150
        )

    explanation = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return explanation
