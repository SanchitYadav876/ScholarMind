# ScholarMind - Deployment Guide

## **🚀 Complete Setup Instructions**

---

## **Part 1: Backend Deployment on Render**

### **Step 1: Create Render Account**
1. Go to https://render.com
2. Sign up with GitHub account (easier login)
3. Create new account

### **Step 2: Prepare Repository**
Your GitHub repo already has:
- ✅ `app.py` - Flask backend
- ✅ `Procfile` - Render configuration
- ✅ `requirements.txt` - Python dependencies
- ✅ `student_pass_lr.joblib` - ML model
- ✅ `student_marks_dataset.csv` - Training data

### **Step 3: Deploy to Render**
1. Log in to Render dashboard
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account
4. Select repository: `ScholarMind`
5. Fill in:
   - **Name**: `scholarwind-api` (or any name)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click **"Create Web Service"**
7. Wait 5-10 minutes for deployment
8. Copy the deployed URL (e.g., `https://scholarwind-api.onrender.com`)

---

## **Part 2: Web Frontend on GitHub Pages**

### **Step 1: Prepare Files**
Your web files are ready:
- `web-assets/index.html` - Landing page with 3D model
- `web-assets/predictor.html` - Predictor interface

### **Step 2: Create GitHub Pages Configuration**

Create file: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to GitHub Pages
        run: |
          mkdir -p docs
          cp web-assets/index.html docs/index.html
          cp web-assets/predictor.html docs/predictor.html
      - uses: actions/upload-artifact@v2
        with:
          name: docs
          path: docs
```

### **Step 3: Enable GitHub Pages**
1. Go to your repo settings
2. Scroll to "GitHub Pages"
3. Source: Select `docs` folder
4. Your site will be live at: `https://SanchitYadav876.github.io/ScholarMind`

---

## **Part 3: Update Mobile App**

### **Update API URL in predictionService.js**

```javascript
// Change this:
const API_BASE_URL = 'http://localhost:5000';

// To this (use your Render URL):
const API_BASE_URL = 'https://scholarwind-api.onrender.com';
```

Then run:
```bash
npm start
```

---

## **Part 4: Build APK for Android**

### **Option A: Using Expo (Easiest)**

```bash
cd mobile-app
npx eas build --platform android
```

Then download APK from Expo dashboard.

### **Option B: Using Release Build (Advanced)**

```bash
cd mobile-app
eas build --platform android --profile preview
```

---

## **Part 5: URLs After Deployment**

| Platform | URL |
|----------|-----|
| **Web Landing** | https://SanchitYadav876.github.io/ScholarMind |
| **Web Predictor** | https://SanchitYadav876.github.io/ScholarMind/predictor.html |
| **API Backend** | https://scholarwind-api.onrender.com |
| **Android APK** | Download from Expo or build locally |

---

## **Part 6: Test Everything**

### **Test Web:**
1. Open https://SanchitYadav876.github.io/ScholarMind
2. Click "Try Now"
3. Fill predictor form
4. Should work offline!

### **Test Mobile:**
1. Install APK on Android phone
2. App should predict results
3. Works with or without laptop running

### **Test API:**
```bash
curl -X GET https://scholarwind-api.onrender.com/statistics
```

Should return JSON stats.

---

## **Important Notes**

⚠️ **Render Free Tier:**
- Free tier spins down after 15 min of no activity
- First request takes 30 sec to wake up
- **Solution**: Upgrade to paid tier ($7/month) for always-on

✅ **GitHub Pages Limitations:**
- Must be public repo
- Cannot run backend code
- Static files only (HTML, CSS, JS)

✅ **Environmental Variables (if needed):**
Add to Render dashboard:
```
API_KEY=your_key_here
DATABASE_URL=your_db_url
```

---

## **Support & Troubleshooting**

| Problem | Solution |
|---------|----------|
| API down after 15 min | Use paid Render tier |
| CORS error | Backend already has CORS enabled |
| APK too large | Remove unused dependencies |
| Web loads but no API | Check Render URL in predictionService.js |

---

## **Next Steps**

1. ✅ Commit all files to GitHub
2. ✅ Enable GitHub Pages in Settings
3. ✅ Deploy backend to Render
4. ✅ Update mobile app API URL
5. ✅ Build and test APK
6. ✅ Share links with everyone!

**Your ScholarMind is now live worldwide!** 🎉
