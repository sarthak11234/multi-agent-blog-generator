# Setting Up HuggingFace API Token (Optional but Recommended)

## Why Get a Token?

- **Better Rate Limits**: Free tier with token has higher limits
- **More Models**: Access to gated/private models
- **Reliability**: More stable service
- **Free**: No cost, just requires account signup

## How to Get Your Free Token

1. **Create Account** (if you don't have one):
   - Go to https://huggingface.co/
   - Click "Sign Up" and create a free account

2. **Generate Token**:
   - Go to https://huggingface.co/settings/tokens
   - Click "New token"
   - Name it (e.g., "capstone-project")
   - Select "Read" permissions (sufficient for inference)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again!)

3. **Set the Token**:

   **Option A: Environment Variable (Recommended)**
   ```bash
   # Windows (PowerShell)
   $env:HF_API_TOKEN="your_token_here"
   
   # Windows (CMD)
   set HF_API_TOKEN=your_token_here
   
   # Linux/Mac
   export HF_API_TOKEN="your_token_here"
   ```

   **Option B: Create .env file in backend/ directory**
   ```bash
   # backend/.env
   HF_API_TOKEN=your_token_here
   ```
   Then install python-dotenv (already in requirements.txt) and the code will auto-load it.

   **Option C: Set in your shell profile** (persists across sessions)
   - Add to your `.bashrc`, `.zshrc`, or PowerShell profile

## Verify It Works

After setting the token and restarting the server, you should see in the logs:
```
Using HuggingFace API token (recommended for better rate limits)
HF Inference client initialized for model: microsoft/Phi-3-mini-4k-instruct
```

## Without Token

The system will still work without a token for many public models, but:
- You may hit rate limits faster
- Some models may not be accessible
- You'll see a warning in the logs

## Security Note

- **Never commit your token to git**
- Add `.env` to `.gitignore` if using that method
- Don't share your token publicly

