import requests
import time
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("Testing /health...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ /health passed")
            return True
        else:
            print(f"❌ /health failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ /health error: {e}")
        return False

def test_generate():
    print("\nTesting /generate (this may take a few seconds)...")
    payload = {"topic": "Python programming", "goal": "Explain basics"}
    try:
        start_time = time.time()
        response = requests.post(f"{BASE_URL}/generate", json=payload, timeout=60)
        duration = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ /generate passed in {duration:.2f}s")
            print(f"   Run ID: {data.get('run_id')}")
            print(f"   Steps: {list(data.get('steps', {}).keys())}")
            return True
        else:
            print(f"❌ /generate failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ /generate error: {e}")
        return False

def test_logs():
    print("\nTesting /logs...")
    try:
        response = requests.get(f"{BASE_URL}/logs")
        if response.status_code == 200:
            logs = response.json().get("logs", [])
            print(f"✅ /logs passed (found {len(logs)} logs)")
            return True
        else:
            print(f"❌ /logs failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ /logs error: {e}")
        return False

def test_memory():
    print("\nTesting /memory...")
    try:
        response = requests.get(f"{BASE_URL}/memory")
        if response.status_code == 200:
            memory = response.json().get("memory", [])
            print(f"✅ /memory passed (found {len(memory)} items)")
            return True
        else:
            print(f"❌ /memory failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ /memory error: {e}")
        return False

if __name__ == "__main__":
    print(f"Starting comprehensive verification on {BASE_URL}\n")
    
    if not test_health():
        print("\n⛔ Health check failed. Aborting.")
        sys.exit(1)
        
    if not test_generate():
        print("\n⛔ Generation failed. Check logs.")
        # Continue to check logs anyway
        
    test_logs()
    test_memory()
    
    print("\nVerification complete.")
