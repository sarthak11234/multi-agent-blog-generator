#!/usr/bin/env python
"""Test InferenceClient directly."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path, override=True)
    print(f"[OK] Loaded .env")

token = os.getenv("HF_API_TOKEN")
print(f"[OK] Token: {token[:10]}..." if token else "[ERROR] No token")

# Test InferenceClient
try:
    from huggingface_hub import InferenceClient
    print("[OK] InferenceClient imported")
    
    # Try GPT2
    print("\nTesting GPT2...")
    client = InferenceClient(model="gpt2", token=token)
    response = client.text_generation("The future of AI is", max_new_tokens=30)
    print(f"[SUCCESS] GPT2 Response: {response}")
    
except Exception as e:
    print(f"[ERROR] GPT2 failed: {e}")
    import traceback
    traceback.print_exc()
    
    # Try a different model
    try:
        print("\nTrying google/flan-t5-base...")
        client = InferenceClient(model="google/flan-t5-base", token=token)
        response = client.text_generation("The future of AI is", max_new_tokens=30)
        print(f"[SUCCESS] Flan-T5 Response: {response}")
    except Exception as e2:
        print(f"[ERROR] Flan-T5 also failed: {e2}")

