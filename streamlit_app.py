import streamlit as st
import tempfile
import os

from inference import generate_explanation

st.set_page_config(page_title="VLM Image Explainer")

st.title("🧠 Vision-Language Model Demo")
st.write("Upload an image and let the model explain it.")
st.info("Note: the model loads on first use and may take a while on CPU. If you see a download/auth error, check the BLIP_MODEL env var or set HF_TOKEN.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Explain Image"):
        # Save to a temp file and ensure cleanup
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        try:
            with st.spinner("Generating explanation (this may take a while on CPU)..."):
                explanation = generate_explanation(temp_path)

            st.subheader("Explanation")
            st.write(explanation)
        except Exception as e:
            # Show helpful error message in the UI
            st.error(f"Failed to generate explanation: {e}")
        finally:
            try:
                os.remove(temp_path)
            except Exception:
                pass
else:
    st.info("Please upload an image to get started.")
