# File: generate_image_offline.py

import sys
from diffusers import StableDiffusionPipeline
import torch
from pathlib import Path

prompt = sys.argv[1] if len(sys.argv) > 1 else "A cat made of galaxies floating in space"

model_path = "/home/ai/models/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float32)
pipe = pipe.to("cpu")

image = pipe(prompt).images[0]

output_dir = Path("/home/ai/ai-assistant/outputs")
output_dir.mkdir(parents=True, exist_ok=True)
image.save(output_dir / "generated_image.png")

print("✅ Image generated and saved offline.")
