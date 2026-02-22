# train_models.py
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# 1. load data (use path relative to this script so running from any cwd works)
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "student_marks_dataset.csv"
df = pd.read_csv(data_path)

# 2. features and target
X = df.drop(columns=["student_id", "result"])
y = df["result"]

# 3. split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. preprocessing: numeric vs categorical
numeric_features = ["marks", "study_hours_per_week", "attendance_percent", "previous_year_marks", "assignments_submitted", "extracurricular_score", "parental_education_level"]
categorical_features = ["school_type"]

numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# 5. Baseline model pipeline (Logistic Regression)
clf_lr = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

clf_lr.fit(X_train, y_train)

# evaluate LR
y_pred_lr = clf_lr.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_lr))
print(confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

# 6. Neural Network (MLP)
clf_mlp = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", MLPClassifier(hidden_layer_sizes=(64,32), max_iter=300, random_state=42))
])

clf_mlp.fit(X_train, y_train)

y_pred_mlp = clf_mlp.predict(X_test)
print("MLP Accuracy:", accuracy_score(y_test, y_pred_mlp))
print(confusion_matrix(y_test, y_pred_mlp))
print(classification_report(y_test, y_pred_mlp))

# 7. RANDOM FOREST - Industry Favourite (NEW!)
print("\n" + "="*80)
print("RANDOM FOREST - 200 Trees (Industry Standard)")
print("="*80)

from sklearn.ensemble import RandomForestClassifier

clf_rf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1))
])

clf_rf.fit(X_train, y_train)

y_pred_rf = clf_rf.predict(X_test)
rf_accuracy = accuracy_score(y_test, y_pred_rf)
print("Random Forest Accuracy:", rf_accuracy)
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf, target_names=['FAIL', 'PASS']))

# 8. FEATURE IMPORTANCE ANALYSIS (NEW!)
print("\n" + "="*80)
print("FEATURE IMPORTANCE - Which features matter most?")
print("="*80)

feature_importance = clf_rf.named_steps['classifier'].feature_importances_
feature_names = numeric_features + ['school_type_private', 'school_type_public']

importance_list = sorted(zip(feature_names, feature_importance), key=lambda x: x[1], reverse=True)

print("\nTop Features by Importance:")
for name, score in importance_list:
    bar = "█" * int(score * 100)
    print(f"{name:30} | {bar} {score:.4f}")

# 9. MODEL COMPARISON TABLE (NEW!)
print("\n" + "="*80)
print("MODEL COMPARISON - PROFESSIONAL METRICS")
print("="*80)

lr_accuracy = accuracy_score(y_test, y_pred_lr)
mlp_accuracy = accuracy_score(y_test, y_pred_mlp)

print(f"\nLogistic Regression:  {lr_accuracy:.4f} ({lr_accuracy*100:.2f}%)")
print(f"Neural Network (MLP): {mlp_accuracy:.4f} ({mlp_accuracy*100:.2f}%)")
print(f"Random Forest:        {rf_accuracy:.4f} ({rf_accuracy*100:.2f}%)")

# 10. Save best model
best_accuracy = max(lr_accuracy, mlp_accuracy, rf_accuracy)
if best_accuracy == rf_accuracy:
    best_model = clf_rf
    model_name = "Random Forest"
    save_name = "student_pass_rf.joblib"
elif best_accuracy == mlp_accuracy:
    best_model = clf_mlp
    model_name = "Neural Network"
    save_name = "student_pass_mlp.joblib"
else:
    best_model = clf_lr
    model_name = "Logistic Regression"
    save_name = "student_pass_lr.joblib"

joblib.dump(best_model, save_name)
print(f"\nBest Model: {model_name} ({best_accuracy*100:.2f}%)")
print(f"Saved to: {save_name}")