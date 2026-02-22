# ScholarMind - Quick Start Guide (QuickStart हिंदी Guide)

## **5 मिनट में Deploy करो! 🚀**

---

## **Step 1: GitHub पर Push करो**

**Windows PowerShell खोलो:**

```powershell
cd "d:\learing python"
```

**फिर ये commands चलाओ:**

```powershell
# Git initialization
git init
git config user.name "Sanchi Yadav"
git config user.email "tum.email@gmail.com"

# Add all files
git add -A

# Commit करो
git commit -m "ScholarMind v1.0 - Deploy ready"

# Push to GitHub (पहली बार login हो सकता है)
git branch -M main
git remote add origin https://github.com/SanchitYadav876/ScholarMind.git
git push -u origin main
```

**Ya bas ये script चलाओ:**
```powershell
.\setup_github.bat
```

---

## **Step 2: GitHub Pages Enable करो**

1. Jao: https://github.com/SanchitYadav876/ScholarMind
2. **Settings** → अंदर जाओ
3. Left sidebar में **Pages** खोजो
4. **Source**: "Deploy from a branch" चुनो
5. **Branch**: `main` चुनो
6. **Folder**: `/docs` चुनो
7. **Save** करो
8. 2-3 मिनट wait करो

**✅ Your website live होगी:**
```
https://SanchitYadav876.github.io/ScholarMind
```

---

## **Step 3: Backend Deploy करो (Optional लेकिन जरूरी)**

### **Render पर (आसान तरीका)**

1. Jao: https://render.com
2. **Sign up** (GitHub से करो)
3. **New +** → **Web Service**
4. **GitHub repository select करो**: ScholarMind
5. Fill करो:
   - **Name**: `scholarwind-api`
   - **Runtime**: Python 3
   - **Build**: `pip install -r requirements.txt`
   - **Start**: `gunicorn app:app`
6. **Create Web Service** क्लिक करो
7. 5-10 मिनट wait करो
8. **Copy करो deploying URL** (जैसे `https://scholarwind-api.onrender.com`)

### **Mobile App में Update करो**

File खोलो: `d:\learing python\mobile-app\services\predictionService.js`

**Line 12 को update करो:**

```javascript
// पहले:
const API_BASE_URL = 'http://localhost:5000';

// अब:
const API_BASE_URL = 'https://scholarwind-api.onrender.com';
```

**Save करो (Ctrl+S)**

---

## **Step 4: Mobile App Build करो (APK)**

```powershell
cd "d:\learing python\mobile-app"

# Build APK for download
npx eas build --platform android --profile preview
```

**या Expo dashboard से download करो automatic**

---

## **Final URLs - काम करना Start करो!**

| **Platform** | **URL** |
|--|--|
| 🌐 **Web Landing** | https://SanchitYadav876.github.io/ScholarMind |
| 📊 **Predictor** | https://SanchitYadav876.github.io/ScholarMind/predictor.html |
| 🔌 **API Backend** | https://scholarwind-api.onrender.com |
| 📱 **Android APK** | Download from Expo or GitHub Releases |

---

## **Testing करো**

### **Web Test करो:**
```bash
# Open browser:
https://SanchitYadav876.github.io/ScholarMind

# Ya local:
python "developing AI/app.py"
# फिर जाओ: http://localhost:5000
```

### **API Test करो:**
```powershell
# Command line से:
curl -X GET "https://scholarwind-api.onrender.com/statistics"

# Response मिलना चाहिए JSON format में
```

### **Mobile Test करो:**
```bash
cd mobile-app
npm start
# Expo Go से QR code scan करो
```

---

## **Common Issues & Fix**

| **Error** | **Fix** |
|--|--|
| `git: command not found` | Install Git: https://git-scm.com |
| `Permission denied` | Right-click PowerShell → Run as Administrator |
| `npm ERR! code ENOENT` | `npm install` चलाओ mobile-app folder में |
| `Render हमेशा down होता है` | Paid tier upgrade करो ($7/month) |
| `CORS error on web` | Backend में CORS पहले से है, फिक्स जरूरत नहीं |
| `Mobile app won't connect` | Check API_BASE_URL in `predictionService.js` |

---

## **Sharing करो**

अब सब को share कर सकते हो:

```
🎓 ScholarMind - AI Student Predictor

Try the web app:
https://SanchitYadav876.github.io/ScholarMind

Download Android APK:
[APK Link]

GitHub:
https://github.com/SanchitYadav876/ScholarMind

79.7% accuracy! Made with ❤️
```

---

## **Next Level - Features Add करो**

1. **More Models** - Add SVM, Gradient Boosting
2. **Database** - Store predictions permanently
3. **User Auth** - Login system
4. **Notifications** - Push alerts for results
5. **Internationalization** - हिंदी support
6. **Mobile Improvements** - iOS support, better UI
7. **Analytics** - Better dashboard

---

## **Support**

कोई issue? Jao:
- GitHub Issues: https://github.com/SanchitYadav876/ScholarMind/issues
- Docs: https://github.com/SanchitYadav876/ScholarMind#readme

---

**🎉 Congrats! ScholarMind is now LIVE worldwide!**

अब सब को बता दो कि तुम्हारे पास AI app है! 🚀
