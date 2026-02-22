# ScholarMind - AI Student Pass/Fail Predictor

![ScholarMind](https://img.shields.io/badge/AI-Powered-blueviolet) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![React Native](https://img.shields.io/badge/React--Native-0.72-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

**Predict whether a student will pass or fail using AI/ML** 🎓

Built with Flask backend, React Native mobile app, and beautiful web interface with 3D animations.

---

## **🚀 Features**

✨ **79.7% Prediction Accuracy** - Advanced ML model trained on 10,000+ student records
📱 **Cross-Platform** - Works on Web, iOS, Android, Windows
🔒 **Privacy First** - All data stored locally, no cloud tracking
⚡ **Offline Support** - App works even without internet
📊 **Real-time Dashboard** - View statistics and visualizations
💾 **Export Data** - Download predictions as CSV
🎨 **Beautiful UI** - 3D animations and modern design

---

## **📲 Try It Online**

| Platform | Link |
|----------|------|
| 🌐 **Web** | [ScholarMind Web App](https://SanchitYadav876.github.io/ScholarMind) |
| 📱 **Android APK** | Coming Soon (Deploy on Render) |
| 💻 **Desktop** | Windows EXE available |

---

## **⚙️ Installation**

### **1. Clone Repository**
```bash
git clone https://github.com/SanchitYadav876/ScholarMind.git
cd ScholarMind
```

### **2. Backend Setup (Python)**
```bash
# Install dependencies
pip install -r requirements.txt

# Train model (one-time only)
python developing\ AI/train_models.py

# Start Flask server
cd developing\ AI
python app.py
```

Server runs on: `http://localhost:5000`

### **3. Web Interface**
```bash
# Open in browser
http://localhost:5000
# or
http://localhost:5000/dashboard
```

### **4. Mobile App (React Native)**
```bash
cd mobile-app

# Install dependencies
npm install

# Fix Expo compatibility
npx expo install --fix

# Start development server
npm start

# On phone: Scan QR code with Expo Go app
```

---

## **📊 How It Works**

1. **Input Student Data**
   - Current marks, study hours, attendance
   - Previous marks, assignments completed
   - Extracurricular activities, parental education
   - School type (private/government)

2. **AI Model Predicts**
   - Logistic Regression (79.7% accuracy)
   - Decision Tree Ensemble
   - Neural Network comparison
   - Probability calculation

3. **See Results**
   - ✅ PASS or ❌ FAIL prediction
   - Pass probability percentage
   - Fail probability percentage
   - Save to local history

4. **View Analytics**
   - Total predictions
   - Pass/fail distribution
   - Success rate statistics
   - Historical data export

---

## **🔧 Configuration**

### **Change API Endpoint**
Edit `mobile-app/services/predictionService.js`:
```javascript
// For localhost (development)
const API_BASE_URL = 'http://localhost:5000';

// For production (Render)
const API_BASE_URL = 'https://yourapi.onrender.com';

// For local network (Android on same WiFi)
const API_BASE_URL = 'http://192.168.1.100:5000';
```

### **Change Model**
Edit `developing AI/app.py`:
```python
# Line 20: Choose model
# MODEL_FILE = 'student_pass_lr.joblib'  # Current (79.7%)
# MODEL_FILE = 'student_pass_rf.joblib'   # Random Forest (78.8%)
# MODEL_FILE = 'student_pass_mlp.joblib'  # Neural Net (76.3%)
```

---

## **🌐 Deployment**

### **Deploy Backend to Render (Free + Hosting)**

1. Push to GitHub
2. Go to [Render.com](https://render.com)
3. Connect GitHub repository
4. Deploy → Choose `developing AI/` folder
5. Get public URL in 5 minutes

### **Deploy Web to GitHub Pages**

1. Enable Pages in repo Settings
2. Choose `docs` folder as source
3. Website goes live at `https://yourusername.github.io/ScholarMind`

### **Build APK for Distribution**

```bash
cd mobile-app
eas build --platform android
# Download from Expo dashboard
```

---

## **📈 Model Performance**

| Algorithm | Accuracy | Precision | Recall |
|-----------|----------|-----------|--------|
| **Logistic Regression** ⭐ | **79.7%** | 81.2% | 76.8% |
| Random Forest | 78.85% | 79.5% | 78.2% |
| Neural Network (MLP) | 76.3% | 77.1% | 75.4% |

**Features Importance:**
- Study Hours: 24.66% ⭐
- Previous Marks: 22.34%
- Attendance: 18.92%
- Current Marks: 15.28%
- Others: 18.8%

---

## **🎨 UI Features**

✅ **3D Animated Models** - Beautiful Three.js animations on web
✅ **Responsive Design** - Works on mobile, tablet, desktop
✅ **Dark/Light Support** - Adaptive color scheme
✅ **Real-time Charts** - Chart.js visualizations
✅ **Offline Functionality** - Works without internet (mobile)
✅ **Local Storage** - Predictions saved locally
✅ **Export Options** - CSV download support

---

## **📁 Project Structure**

```
ScholarMind/
├── developing AI/
│   ├── app.py                 # Flask backend
│   ├── train_models.py        # ML model training
│   ├── templates/
│   │   ├── index.html        # Web predictor
│   │   └── dashboard.html    # Analytics dashboard
│   └── student_marks_dataset.csv
│
├── mobile-app/
│   ├── App.js                # React Native entry
│   ├── package.json
│   ├── app.json
│   ├── screens/
│   │   ├── PredictorScreen.js
│   │   ├── DashboardScreen.js
│   │   └── HistoryScreen.js
│   └── services/
│       └── predictionService.js
│
├── web-assets/
│   ├── index.html            # Landing page (3D)
│   └── predictor.html        # Web app
│
├── requirements.txt
├── Procfile                  # Heroku/Render
└── README.md
```

---

## **🐛 Troubleshooting**

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Port 5000 already in use` | Kill process: `lsof -i :5000` then `kill -9 PID` |
| `npm ERR! code ENOENT` | Run `npm install` in mobile-app folder |
| `CORS error` | Backend has CORS enabled, check frontend URL |
| `Expo Go won't connect` | Phone and laptop on same WiFi, check IP address |
| `APK installation fails` | Enable "Unknown sources" in Android settings |

---

## **🤝 Contributing**

Contributions welcome! Fork → Branch → Commit → PR

Ideas:
- Add more ML models
- Improve UI/UX
- Add more features
- Better documentation
- Deploy guide improvements

---

## **📝 License**

MIT License - Feel free to use for projects, education, or commercial use

---

## **👨‍💻 Developer**

**Sanchi Yadav** (@SanchitYadav876)

🔗 [GitHub](https://github.com/SanchitYadav876) | 📧 [Contact](mailto:sanchityadav876@gmail.com)

---

## **🙏 Acknowledgments**

- scikit-learn for ML algorithms
- Flask for backend framework
- React Native & Expo for mobile
- Chart.js for visualizations
- Three.js for 3D animations

---

**Made with ❤️ by Students for Students**

⭐ If helpful, please star this repo!
