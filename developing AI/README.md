# Student Pass/Fail Prediction AI

A production-ready AI model that predicts whether a student will pass or fail based on their academic metrics.

## Features

✅ **AI Model** - 79.7% accurate prediction using Logistic Regression  
✅ **Web Interface** - Beautiful UI for making predictions  
✅ **Database** - All predictions saved to SQLite database  
✅ **Dashboard** - Real-time analytics with charts and statistics  
✅ **CSV Export** - Download all predictions as CSV  
✅ **Ready for Deploy** - Heroku/online deployment configured  

## Quick Start

### Local Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the Flask app
python app.py

# 3. Open in browser
http://localhost:5000
```

### Usage

1. **Make Predictions**
   - Go to `http://localhost:5000`
   - Fill in student details
   - Click "Predict Result"
   - Get instant PASS/FAIL prediction with probabilities

2. **View Dashboard**
   - Go to `http://localhost:5000/dashboard`
   - See real-time statistics
   - View charts for pass/fail distribution
   - See prediction history

3. **Export Data**
   - Click "Download as CSV" on dashboard
   - All predictions export to CSV file

## Files Structure

```
developing AI/
├── app.py                    # Flask backend
├── # train_models.py         # Model training script
├── student_marks_dataset.csv # Training data
├── student_pass_lr.joblib    # Best trained model
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku deployment config
├── predictions.db            # SQLite database (auto-created)
└── templates/
    ├── index.html            # Predictor page
    └── dashboard.html        # Analytics dashboard
```

## Model Details

- **Algorithm**: Logistic Regression
- **Accuracy**: 79.70%
- **Features**: 8 input features
  - Marks
  - Study hours/week
  - Attendance %
  - Previous year marks
  - Assignments submitted
  - Extracurricular score
  - Parental education level
  - School type

### Feature Importance

1. Study hours/week: 24.66% (MOST IMPORTANT!)
2. Marks: 16.25%
3. Previous year marks: 16.15%
4. Attendance: 14.47%
5. Others: < 10%

## Deploy Online

### Option 1: Heroku (Free Tier)

```bash
# 1. Install Heroku CLI
# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Deploy
git push heroku main

# 5. Your app is live!
https://your-app-name.herokuapp.com
```

### Option 2: PythonAnywhere

1. Sign up at pythonanywhere.com
2. Upload files to server
3. Configure web app
4. Your app is live!

### Option 3: AWS / Google Cloud / Azure

1. Create EC2/App Engine/App Service instance
2. Install Python and dependencies
3. Deploy Flask app
4. Enable HTTPS
5. Your app is ready!

## API Endpoints

- `GET /` - Main predictor page
- `POST /predict` - Make prediction
  ```json
  {
    "marks": 75,
    "study_hours": 10,
    "attendance": 85,
    "previous_marks": 78,
    "assignments": 8,
    "extracurricular": 7,
    "parental_education": 2,
    "school_type": "private"
  }
  ```
- `GET /dashboard` - Analytics dashboard
- `GET /history` - Get prediction history (JSON)
- `GET /statistics` - Get statistics (JSON)
- `GET /export` - Download predictions as CSV

## Database

SQLite database (`predictions.db`) stores:
- Timestamp
- Student features (marks, attendance, etc.)
- Prediction (PASS/FAIL)
- Pass/Fail probability percentages

## Requirements

- Python 3.8+
- Flask 3.1.2
- scikit-learn 1.3.1
- pandas 2.0.3
- numpy 1.24.3
- joblib 1.3.1

## Screenshots

### Predictor Page
- Clean, modern UI
- Real-time predictions
- Shows probability percentages

### Dashboard
- Pass/Fail statistics
- Distribution charts
- Prediction history table
- CSV export button

## Future Enhancements

- [ ] Add login/authentication
- [ ] Multiple model comparison
- [ ] Advanced filtering
- [ ] Data visualization improvements
- [ ] Mobile app
- [ ] Batch predictions

## License

MIT License - Feel free to use and modify!

## Support

For issues or questions, create an issue in the repository.
