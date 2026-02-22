from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import warnings
import sqlite3
from datetime import datetime
import json
import io

warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

# Database initialization
DATABASE = Path(__file__).resolve().parent / "predictions.db"

def init_db():
    """Initialize database"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        marks REAL,
        study_hours REAL,
        attendance REAL,
        previous_marks REAL,
        assignments REAL,
        extracurricular REAL,
        parental_education REAL,
        school_type TEXT,
        prediction TEXT,
        pass_probability REAL,
        fail_probability REAL
    )''')
    conn.commit()
    conn.close()

def save_prediction(data, prediction, pass_prob, fail_prob):
    """Save prediction to database"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''INSERT INTO predictions 
                (timestamp, marks, study_hours, attendance, previous_marks, 
                 assignments, extracurricular, parental_education, school_type,
                 prediction, pass_probability, fail_probability)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (datetime.now().isoformat(),
               data['marks'], data['study_hours'], data['attendance'],
               data['previous_marks'], data['assignments'],
               data['extracurricular'], data['parental_education'],
               data['school_type'], prediction, pass_prob, fail_prob))
    conn.commit()
    conn.close()

def get_predictions_history(limit=50):
    """Get prediction history"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM predictions ORDER BY timestamp DESC LIMIT ?', (limit,))
    cols = [description[0] for description in c.description]
    rows = c.fetchall()
    conn.close()
    return [dict(zip(cols, row)) for row in rows]

def get_statistics():
    """Get prediction statistics"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    c.execute('SELECT COUNT(*) FROM predictions')
    total = c.fetchone()[0]
    
    c.execute('SELECT COUNT(*) FROM predictions WHERE prediction = ?', ('PASS',))
    passed = c.fetchone()[0]
    
    c.execute('SELECT AVG(pass_probability) FROM predictions')
    avg_pass_prob = c.fetchone()[0] or 0
    
    conn.close()
    
    return {
        'total_predictions': total,
        'pass_count': passed,
        'fail_count': total - passed,
        'pass_rate': (passed / total * 100) if total > 0 else 0,
        'avg_pass_probability': avg_pass_prob
    }

# Initialize database on startup
init_db()

# Load the trained model (best model from training)
script_dir = Path(__file__).resolve().parent
model_path = script_dir / "student_pass_lr.joblib"  # Updated to use best model
if not model_path.exists():
    # Fallback to MLP if LR doesn't exist
    model_path = script_dir / "student_pass_mlp.joblib"
model = joblib.load(model_path)
print(f"Loaded model from: {model_path.name}")

@app.route('/')
def index():
    """Render the home page with prediction form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint to make predictions"""
    try:
        # Get data from form
        data = request.json
        
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        print(f"Received prediction request: {data}")
        
        # Create DataFrame with correct column names to match training data
        input_df = pd.DataFrame({
            'marks': [float(data['marks'])],
            'study_hours_per_week': [float(data['study_hours'])],
            'attendance_percent': [float(data['attendance'])],
            'previous_year_marks': [float(data['previous_marks'])],
            'assignments_submitted': [float(data['assignments'])],
            'extracurricular_score': [float(data['extracurricular'])],
            'parental_education_level': [float(data['parental_education'])],
            'school_type': [data['school_type']]
        })
        
        print(f"Input DataFrame:\n{input_df}")
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]
        
        pass_prob = round(float(probability[1]) * 100, 2)
        fail_prob = round(float(probability[0]) * 100, 2)
        
        print(f"Prediction: {prediction}, Probabilities: {probability}")
        
        # Save to database
        save_prediction(data, 'PASS' if prediction == 1 else 'FAIL', pass_prob, fail_prob)
        
        # Format response
        result = {
            'success': True,
            'prediction': 'PASS' if prediction == 1 else 'FAIL',
            'pass_probability': pass_prob,
            'fail_probability': fail_prob,
            'color': 'green' if prediction == 1 else 'red'
        }
        
        return jsonify(result)
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/history')
def history():
    """Get prediction history"""
    try:
        history_data = get_predictions_history()
        return jsonify({'success': True, 'predictions': history_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/statistics')
def statistics():
    """Get prediction statistics"""
    try:
        stats = get_statistics()
        return jsonify({'success': True, 'statistics': stats})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/export')
def export_csv():
    """Export predictions as CSV"""
    try:
        conn = sqlite3.connect(DATABASE)
        df = pd.read_sql_query("SELECT * FROM predictions ORDER BY timestamp DESC", conn)
        conn.close()
        
        # Create CSV in memory
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        
        return send_file(
            io.BytesIO(csv_buffer.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='predictions.csv'
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/dashboard')
def dashboard():
    """Render dashboard page"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    print("Student Pass/Fail Predictor AI")
    print("Starting Flask app on http://localhost:5000")
    print("Open your browser and navigate to http://localhost:5000")
    app.run(debug=True, port=5000)
