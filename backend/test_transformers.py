#!/usr/bin/env python
"""Test if transformers is working."""

try:
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
    print("[OK] Transformers imported successfully")
    print(f"AutoModelForCausalLM: {AutoModelForCausalLM is not None}")
    print(f"AutoTokenizer: {AutoTokenizer is not None}")
    print(f"pipeline: {pipeline is not None}")
except Exception as e:
    print(f"[ERROR] Failed to import transformers: {e}")
    import traceback
    traceback.print_exc()

