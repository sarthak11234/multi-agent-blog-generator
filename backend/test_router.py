#!/usr/bin/env python
"""Test router endpoint formats."""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, override=True)

token = os.getenv("HF_API_TOKEN")
model = "google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
} if token else {"Content-Type": "application/json"}

# Try different router endpoint formats
endpoints = [
    f"https://router.huggingface.co/hf-inference/models/{model}",
    f"https://router.huggingface.co/hf-inference/v1/models/{model}",
    f"https://router.huggingface.co/hf-inference/v1/{model}",
    f"https://router.huggingface.co/models/{model}",
]

payload = {
    "inputs": "Translate to English: Hola mundo",
    "parameters": {"max_new_tokens": 50}
}

for endpoint in endpoints:
    print(f"\nTesting: {endpoint}")
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"[SUCCESS] {response.json()}")
            break
        else:
            print(f"Response: {response.text[:200]}")
    except Exception as e:
        print(f"Error: {e}")

