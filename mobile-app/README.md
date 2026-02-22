# Student Pass/Fail Predictor - Mobile App

A React Native mobile application for iOS and Android that connects to your AI prediction API.

## Features

✅ **Make Predictions** - Beautiful form to input student data  
✅ **Real-time Results** - Instant PASS/FAIL predictions with probabilities  
✅ **Dashboard** - View statistics and pass/fail distribution charts  
✅ **History** - Track all predictions locally  
✅ **Offline Support** - Works without internet connection using local storage  
✅ **Cross-Platform** - Works on iOS and Android  

## Installation

### 1. Prerequisites

Install these first:
- **Node.js** (v14+): https://nodejs.org/
- **Expo CLI**: `npm install -g expo-cli`
- **Expo Go App** on your phone (from App Store or Google Play)

### 2. Setup

```bash
# Navigate to mobile app directory
cd "d:\learing python\mobile-app"

# Install dependencies
npm install

# OR if npm install fails, use yarn
npm install -g yarn
yarn install
```

### 3. Configure API URL

Edit `services/predictionService.js` and change:

```javascript
// For local development (simulator only):
const API_BASE_URL = 'http://localhost:5000';

// For physical device or production, use your deployed server:
const API_BASE_URL = 'https://your-deployed-app.herokuapp.com';
```

### 4. Run the App

```bash
# Start Expo development server
npm start
# Or: expo start

# Then press:
# i  - Open on iOS simulator
# a  - Open on Android emulator
# w  - Open on web
# s  - Send to phone (scan QR code with Expo Go app)
```

## Running on Physical Device

### iOS:
1. Download **Expo Go** from App Store
2. Run `npm start`
3. Scan QR code with Expo Go
4. App opens on your phone!

### Android:
1. Download **Expo Go** from Google Play
2. Run `npm start`
3. Scan QR code with Expo Go
4. App opens on your phone!

**Note:** If using physical device, change API_BASE_URL to your deployed server (Heroku, AWS, etc.)

## Deploy to App Stores

### iOS (Apple App Store)

```bash
# Create account at developer.apple.com ($99/year)
# Then run:
eas build --platform ios
# Follow instructions to submit
```

### Android (Google Play Store)

```bash
# Create account at play.google.com ($25 one-time)
# Then run:
eas build --platform android
# Generate signed APK/AAB and upload
```

## File Structure

```
mobile-app/
├── App.js                  # Main app entry
├── package.json            # Dependencies
├── app.json                # Expo config
├── services/
│   └── predictionService.js  # API communication + local storage
└── screens/
    ├── PredictorScreen.js    # Prediction form
    ├── DashboardScreen.js    # Charts & statistics
    └── HistoryScreen.js      # Prediction history
```

## Features Explained

### Predictor Screen
- Input all 8 student metrics
- Real-time validation
- Beautiful result cards
- Shows pass/fail probabilities

### Dashboard
- Total predictions count
- Pass/fail statistics
- Pie chart visualization
- Average pass probability
- Pull to refresh

### History Screen
- All past predictions
- Sorted by newest first
- Tap to view details
- Clear history option
- Works offline

## API Connection

The app connects to your Flask backend:

```
Predictor Screen → POST /predict
Dashboard Screen → GET /statistics
History Screen   → GET /history
```

All responses are cached locally for offline support.

## Troubleshooting

### "Cannot connect to server"
- Ensure Flask backend is running on `http://localhost:5000`
- For physical device, use deployed server URL
- Check `services/predictionService.js` API_BASE_URL

### "Blank screen on startup"
- Clear cache: `npm start --clear`
- Clear Expo data: `expo start --clear`

### "Errors on Android emulator"
- Enable internet access in emulator settings
- Restart emulator
- Use `10.0.2.2` instead of `localhost` for API_BASE_URL

### "App won't run"
```bash
# Clear and reinstall
rm -rf node_modules
npm install
npm start --clear
```

## Dependencies

- React Native 0.72.5
- Expo 49
- React Navigation 6
- Axios (HTTP client)
- React Native Chart Kit (charts)
- AsyncStorage (local data)

## Building & Distribution

### Create APK/Debug Build:
```bash
eas build --platform android --profile preview
```

### Create Production Build:
```bash
eas build --platform android --profile production
```

### For iOS:
```bash
eas build --platform ios --profile production
```

## Tips & Best Practices

1. **Before deploying** - Change API_BASE_URL to your server
2. **Local development** - Use simulator on same machine
3. **Physical testing** - Use deployed server URL
4. **App store submission** - Need developer accounts ($99 iOS, $25 Android)
5. **Version updates** - Update `version` in `app.json`

## API Response Format

The app expects responses in this format:

```json
{
  "success": true,
  "prediction": "PASS",
  "pass_probability": 87.5,
  "fail_probability": 12.5
}
```

## Future Enhancements

- [ ] Push notifications for predictions
- [ ] Student profile management
- [ ] Compare multiple students
- [ ] Share prediction reports
- [ ] Dark mode support
- [ ] Multi-language support

## Support

For issues:
1. Check Flask backend is running
2. Verify API URL in predictionService.js
3. Check network connectivity
4. Review error messages in console

## License

MIT License - Free to use and modify!
