#!/usr/bin/env python
"""Simple test of HuggingFace API with direct HTTP."""

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

url = f"https://api-inference.huggingface.co/models/{model}"

payload = {
    "inputs": "Translate to English: Hola mundo",
    "parameters": {"max_new_tokens": 50}
}

print(f"Testing: {url}")
print(f"Model: {model}")
print(f"Token: {token[:10]}..." if token else "No token")

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    print(f"\nStatus: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"[SUCCESS] Response: {result}")
    elif response.status_code == 503:
        print("[INFO] Model is loading (503)")
        error_info = response.json()
        print(f"Info: {error_info}")
    elif response.status_code == 410:
        print("[ERROR] Endpoint deprecated (410)")
        print(f"Response: {response.text}")
    else:
        print(f"[ERROR] {response.status_code}")
        print(f"Response: {response.text[:500]}")
except Exception as e:
    print(f"[ERROR] Exception: {e}")
    import traceback
    traceback.print_exc()

