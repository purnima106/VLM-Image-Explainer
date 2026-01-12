# app.py

from inference import generate_explanation

if __name__ == "__main__":
    print("VLM Image Explainer (BLIP-2, CPU-only)")
    print("-" * 40)

    image_path = input("Enter path to image (png/jpg): ").strip()

    result = generate_explanation(image_path)

    print("\n--- Explanation ---\n")
    print(result)
