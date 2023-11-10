from transformers import AutoProcessor, BarkModel
import torch
import scipy
import os
import random

# input
text_prompt = "What’s a man’s favorite thing that starts with M and ends with arriage? Miscarriage! [laughter]"

# load model and processor
model = BarkModel.from_pretrained("suno/bark-small")
processor = AutoProcessor.from_pretrained("suno/bark-small")
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# process the text and pass as model input
inputs = processor(text_prompt)
speech_output = model.generate(**inputs.to(device))

# file output
if not os.path.exists("bark-outputs"):
    os.makedirs("bark-outputs")
scipy.io.wavfile.write(f"bark-outputs/{random.randint(100, 1000)}.wav", rate=model.generation_config.sample_rate, data=speech_output[0].cpu().numpy())