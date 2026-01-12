# model.py

import os
from transformers import BlipProcessor, BlipForConditionalGeneration

# You can override the model id or local path by setting the BLIP_MODEL env variable
MODEL_NAME = os.getenv("BLIP_MODEL", "Salesforce/blip-image-captioning-base")
# Optional token for private models (set via environment variable HF_TOKEN or via `huggingface-cli login`)
HF_TOKEN = os.getenv("HF_TOKEN")

def load_model():
    """Load and return (model, processor).

    Raises a RuntimeError with actionable guidance if loading fails.
    """
    try:
        kwargs = {}
        if HF_TOKEN:
            kwargs["use_auth_token"] = HF_TOKEN

        processor = BlipProcessor.from_pretrained(MODEL_NAME, **kwargs)
        model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME, **kwargs)
        model.eval()
        return model, processor
    except Exception as e:
        msg = (
            f"Failed to load model '{MODEL_NAME}': {e}\n\n"
            "Possible reasons:\n"
            "- Model id is incorrect or not available on Hugging Face.\n"
            "- The model is private and requires authentication. If so, run `huggingface-cli login` or set the HF_TOKEN env var.\n\n"
            "You can override the model by setting the BLIP_MODEL environment variable to a public model id or a local model path."
        )
        raise RuntimeError(msg) from e
