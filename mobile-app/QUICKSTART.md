# Mobile App Quick Start

## 5-Minute Setup

### Step 1: Install Node.js and Expo CLI (3 min)

```powershell
# Download Node.js: https://nodejs.org/ (v14+)
# Then install Expo CLI globally:
npm install -g expo-cli
```

### Step 2: Navigate to mobile app directory

```powershell
cd "d:\learing python\mobile-app"
```

### Step 3: Install dependencies (2 min)

```powershell
npm install
```

If npm install fails:
```powershell
npm install -g yarn
yarn install
```

### Step 4: Start the app

```powershell
npm start
```

You should see:
```
Expo Go URL: exp://localhost:19000
Tunnel URL: [QR code]
```

### Step 5: Test on Simulator/Device

**Option A: iOS Simulator**
```
Press: i
```

**Option B: Android Emulator**
```
Press: a
```

**Option C: Physical Phone**
1. Download "Expo Go" from App Store or Google Play
2. Scan the QR code shown in terminal
3. App opens on your phone!

## Configure API Connection

Edit `services/predictionService.js`:

### For Local Development (Simulator):
```javascript
const API_BASE_URL = 'http://localhost:5000';
```

### For Physical Device:
```javascript
// Get your computer IP address:
// Windows: cmd → ipconfig → IPv4 Address
// Replace 192.168.x.x with your actual IP
const API_BASE_URL = 'http://192.168.x.x:5000';
```

### For Deployed Server:
```javascript
const API_BASE_URL = 'https://your-app.herokuapp.com';
```

## Test the App

1. **Make a Prediction**
   - Go to "Predictor" tab
   - Fill in student data
   - Click "Predict Result"
   - See instant PASS/FAIL!

2. **View Dashboard**
   - Go to "Dashboard" tab
   - See statistics and charts
   - Pull to refresh

3. **Check History**
   - Go to "History" tab
   - See all predictions
   - Swipe to delete

## Common Issues

| Issue | Solution |
|-------|----------|
| "Connection refused" | Make sure Flask server is running: `python app.py` |
| "Blank screen" | Press `r` in terminal to reload, or `npm start --clear` |
| "Cannot find module" | Run `npm install` again |
| "QR code not working" | Make sure Expo Go is installed on phone |
| "Android emulator stuck" | Restart emulator, use `10.0.2.2` instead of `localhost` |

## File Structure

```
mobile-app/
├── App.js                           # Main app
├── package.json                     # Dependencies
├── services/predictionService.js    # API connection
└── screens/
    ├── PredictorScreen.js           # Input form
    ├── DashboardScreen.js           # Charts
    └── HistoryScreen.js             # History list
```

## Flask Backend Setup

Make sure Flask is running before testing:

```powershell
cd "d:\learing python\developing AI"
python app.py
# Should show: "Starting Flask app on http://localhost:5000"
```

## Deploy to Cloud (Optional)

### Option 1: Heroku (Flask Backend)
```bash
cd developing-AI
heroku login
heroku create your-app-name
git push heroku main
# Your API: https://your-app-name.herokuapp.com
```

### Option 2: AWS / Google Cloud / Azure
Follow their Python deployment guides.

## Next Steps

✅ Customize the app branding
✅ Add more features (student profiles, batch predictions, etc.)
✅ Deploy Flask backend to cloud
✅ Build release APK/IPA for app stores
✅ Submit to Google Play & Apple App Store

## Support Commands

```powershell
# Clear cache and reload
npm start --clear

# Kill the server
Ctrl+C

# Reinstall dependencies
rm -r node_modules
npm install

# Check if everything is working
npm start
# Then press 'w' to open web version
```

You're all set! 🚀
