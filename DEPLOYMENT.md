# 🚀 Deployment Guide - FREE Hosting

This guide will help you deploy your Multi-Agent Blog Generator to **Vercel (Frontend)** and **Render (Backend)** for **100% FREE**.

## 📋 Prerequisites

- GitHub account (already done ✅)
- Vercel account (free)
- Render account (free)

---

## 🎨 Part 1: Deploy Frontend to Vercel

### Step 1: Create Vercel Account
1. Go to https://vercel.com
2. Click "Sign Up"
3. Sign up with your GitHub account

### Step 2: Deploy Frontend
1. Click "Add New Project"
2. Import your GitHub repository: `multi-agent-blog-generator`
3. Configure project:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Click "Deploy"
5. Wait 2-3 minutes for deployment to complete

### Step 3: Get Your Frontend URL
- After deployment, you'll get a URL like: `https://multi-agent-blog-generator.vercel.app`
- Copy this URL, you'll need it later!

---

## 🔧 Part 2: Deploy Backend to Render

### Step 1: Create Render Account
1. Go to https://render.com
2. Click "Get Started"
3. Sign up with your GitHub account

### Step 2: Deploy Backend
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `multi-agent-blog-generator`
3. Configure service:
   - **Name**: `multi-agent-blog-backend`
   - **Root Directory**: `backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: Free
4. Add Environment Variables:
   - Click "Advanced" → "Add Environment Variable"
   - Add: `LLM_MODE` = `hf_api`
   - Add: `HF_API_TOKEN` = `your_token_here` (optional, Mock LLM works without it)
5. Click "Create Web Service"
6. Wait 5-10 minutes for deployment

### Step 3: Get Your Backend URL
- After deployment, you'll get a URL like: `https://multi-agent-blog-backend.onrender.com`
- Copy this URL!

---

## 🔗 Part 3: Connect Frontend to Backend

### Step 1: Update Frontend Environment Variable
1. Go to your Vercel project dashboard
2. Click "Settings" → "Environment Variables"
3. Add new variable:
   - **Name**: `VITE_API_BASE`
   - **Value**: `https://multi-agent-blog-backend.onrender.com` (your Render URL)
4. Click "Save"

### Step 2: Redeploy Frontend
1. Go to "Deployments" tab
2. Click "..." on the latest deployment
3. Click "Redeploy"
4. Wait 2-3 minutes

---

## ✅ Part 4: Test Your Deployment

1. Visit your Vercel URL: `https://multi-agent-blog-generator.vercel.app`
2. Enter a topic and click "Generate Content"
3. **Note**: First request may take 30-60 seconds (Render free tier spins down after 15 min)
4. Subsequent requests will be faster!

---

## 🎉 You're Done!

Your app is now live and accessible from anywhere in the world!

**Frontend URL**: https://multi-agent-blog-generator.vercel.app
**Backend URL**: https://multi-agent-blog-backend.onrender.com

---

## 📝 Important Notes

### Free Tier Limitations:
- **Render**: Backend sleeps after 15 minutes of inactivity
  - First request after sleep takes ~30-60 seconds to wake up
  - 512MB RAM limit
  - 750 hours/month (enough for most use cases)

- **Vercel**: 
  - Unlimited bandwidth
  - 100GB bandwidth/month
  - Perfect for frontend hosting

### Tips:
- Keep your backend awake by pinging it every 10 minutes (use a service like UptimeRobot)
- For production, consider upgrading to paid tiers ($7-10/month)

---

## 🐛 Troubleshooting

### Backend not responding:
- Wait 30-60 seconds for it to wake up
- Check Render logs for errors

### Frontend can't connect to backend:
- Verify `VITE_API_BASE` environment variable is set correctly
- Make sure backend URL doesn't have trailing slash

### CORS errors:
- Backend already has CORS configured for all origins
- Should work out of the box

---

## 🔄 Future Updates

To deploy updates:
1. Push changes to GitHub
2. Vercel and Render will auto-deploy
3. No manual steps needed!

---

**Need help?** Check the logs in Vercel/Render dashboards or contact support.
