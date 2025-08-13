# # # # ~/ai-assistant/scripts/generate_image.py

# # # import torch
# # # from diffusers import StableDiffusionPipeline
# # # import os

# # # # 1. Get user input
# # # prompt = input("🖼️ Enter your image prompt: ")

# # # # 2. Load model
# # # print("🚀 Loading Stable Diffusion model... (this may take a few seconds)")
# # # pipe = StableDiffusionPipeline.from_pretrained(
# # #     "runwayml/stable-diffusion-v1-5", 
# # #     torch_dtype=torch.float32
# # # )

# # # # 3. Use CPU or GPU if available
# # # device = "cuda" if torch.cuda.is_available() else "cpu"
# # # pipe = pipe.to(device)

# # # # 4. Generate image
# # # print(f"🎨 Generating image for prompt: '{prompt}'")
# # # image = pipe(prompt).images[0]

# # # # 5. Save image to outputs
# # # output_dir = os.path.expanduser("~/ai-assistant/outputs")
# # # os.makedirs(output_dir, exist_ok=True)
# # # output_path = os.path.join(output_dir, "generated_image.png")
# # # image.save(output_path)

# # # print(f"✅ Image saved to {output_path}")

# # import sys
# # from diffusers import StableDiffusionPipeline
# # import torch
# # from langchain_community.llms import Ollama

# # # Get prompt from CLI args
# # prompt = sys.argv[1] if len(sys.argv) > 1 else "A futuristic city at sunset with neon lights"

# # pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
# # pipe = pipe.to("cpu")  # or .to("cuda") if GPU available

# # image = pipe(prompt).images[0]
# # image.save("/home/ai/ai-assistant/outputs/generated_image.png")
# # print(f"✅ Image generated for prompt: {prompt}")

# # scripts/generate_image.py
# import torch
# from diffusers import StableDiffusionPipeline
# import os
# import sys

# def generate_image(prompt="A futuristic city at sunset with neon lights"):
#     print(f"🔮 Generating image for prompt: {prompt}")
    
#     # Load the model (only once; use caching to avoid repeated downloads)
#     model_id = "runwayml/stable-diffusion-v1-5"
#     pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
#     pipe = pipe.to("cpu")

#     image = pipe(prompt).images[0]

#     output_path = os.path.expanduser("~/ai-assistant/outputs/generated_image.png")
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     image.save(output_path)

#     print(f"✅ Image saved to: {output_path}")

# # Allow running as a standalone script
# if __name__ == "__main__":
#     prompt = sys.argv[1] if len(sys.argv) > 1 else "A futuristic city at sunset with neon lights"
#     generate_image(prompt)
# scripts/generate_image.py

import torch
from diffusers import StableDiffusionPipeline
import os
import sys
from datetime import datetime
import re

def sanitize_filename(text):
    # Remove special characters and limit length to avoid OS filename issues
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[\s_-]+', '_', text)[:50]  # Limit to 50 chars for safety

def generate_image(prompt="A futuristic city at sunset with neon lights"):
    print(f"🔮 Generating image for prompt: {prompt}")
    
    # Load model (cached automatically by HuggingFace)
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")  # Use "cuda" if you have GPU support

    # Generate image
    image = pipe(prompt).images[0]

    # Create timestamped and safe filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_prompt = sanitize_filename(prompt)
    filename = f"{timestamp}_{safe_prompt}.png"

    # Output directory
    output_dir = os.path.expanduser("~/ai-assistant/outputs")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)
    image.save(output_path)

    print(f"✅ Image saved to: {output_path}")

# Run standalone from CLI
if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "A futuristic city at sunset with neon lights"
    generate_image(prompt)