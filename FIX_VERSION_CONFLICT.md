# Fix Version Conflict

## Problem
The `transformers` library requires `huggingface-hub>=0.19.3,<1.0`, but version 1.1.4 is installed, causing import errors.

## Solution

Run this command in your backend directory:

```bash
cd backend
.venv\Scripts\activate
pip install 'huggingface-hub>=0.19.3,<1.0' --force-reinstall
```

Or reinstall all requirements:

```bash
pip install -r requirements.txt --force-reinstall
```

## After Fixing

1. Restart the server
2. Try generating content again
3. The model should now load properly

The first generation will download the model (takes a few minutes), then it will be cached for faster subsequent requests.

