#!/usr/bin/env python
"""Test script to verify HuggingFace Inference API connection."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path, override=True)
    print(f"[OK] Loaded .env from {env_path}")
else:
    print(f"[ERROR] .env not found at {env_path}")

# Check token
token = os.getenv("HF_API_TOKEN")
if token:
    print(f"[OK] HF_API_TOKEN found: {token[:10]}...")
else:
    print("[ERROR] HF_API_TOKEN not found!")
    exit(1)

# Test InferenceClient
try:
    from huggingface_hub import InferenceClient
    print("[OK] huggingface_hub imported successfully")
except ImportError as e:
    print(f"[ERROR] Failed to import huggingface_hub: {e}")
    exit(1)

# Initialize client
model_id = os.getenv("HF_API_MODEL_ID", "microsoft/Phi-3-mini-4k-instruct")
print(f"\nTesting with model: {model_id}")

try:
    client = InferenceClient(model=model_id, token=token)
    print("[OK] InferenceClient initialized")
except Exception as e:
    print(f"[ERROR] Failed to initialize client: {e}")
    exit(1)

# Test generation
print("\nTesting text generation...")
try:
    response = client.text_generation(
        "Hello, this is a test. Please respond with: 'API is working!'",
        max_new_tokens=50,
        temperature=0.7,
    )
    print(f"[OK] Generation successful!")
    print(f"Response: {response[:200]}")
except Exception as e:
    print(f"[ERROR] Generation failed: {e}")
    print(f"Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n[SUCCESS] All tests passed! HuggingFace API is working correctly.")

