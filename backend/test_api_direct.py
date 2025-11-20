#!/usr/bin/env python
"""Direct test of HuggingFace API endpoints."""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path, override=True)
    print(f"[OK] Loaded .env")

token = os.getenv("HF_API_TOKEN")
headers = {"Authorization": f"Bearer {token}"} if token else {}

# Test with GPT2 (simple, reliable model)
model = "gpt2"
test_prompt = "The future of AI is"

# Try different endpoint formats
endpoints = [
    f"https://router.huggingface.co/hf-inference/v1/models/{model}",
    f"https://api-inference.huggingface.co/models/{model}",
]

for endpoint in endpoints:
    print(f"\nTesting: {endpoint}")
    try:
        payload = {
            "inputs": test_prompt,
            "parameters": {"max_new_tokens": 50, "return_full_text": False}
        }
        response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"[SUCCESS] Response: {result}")
            break
        else:
            print(f"Error: {response.text[:200]}")
    except Exception as e:
        print(f"Exception: {e}")

