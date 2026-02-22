# generate_dataset.py
import numpy as np
import pandas as pd

np.random.seed(42)  # reproducible

N = 10000
student_id = np.arange(1, N+1)

# marks: normal distribution, clipped to 0-100
marks = np.random.normal(loc=60, scale=18, size=N).round().astype(int)
marks = np.clip(marks, 0, 100)

# study hours per week: skewed right (exponential-ish) clipped 0-40
study_hours = np.random.exponential(scale=4, size=N)
study_hours = np.clip(study_hours, 0, 40).round(2)

# attendance percent: beta-like distribution skewed to high attendance
attendance = (np.random.beta(a=5, b=1.5, size=N) * 60 + 40).round().astype(int)
attendance = np.clip(attendance, 40, 100)

# previous year marks: correlated with current marks + noise
previous_marks = (marks + np.random.normal(0, 10, size=N)).round().astype(int)
previous_marks = np.clip(previous_marks, 0, 100)

# assignments_submitted: Poisson-like
assignments = np.random.poisson(lam=6, size=N)
assignments = np.clip(assignments, 0, 10)

# extracurricular score (0-10)
extracurricular = np.random.randint(0, 11, size=N)

# parental education (0-4)
parent_edu = np.random.choice([0,1,2,3,4], size=N, p=[0.05,0.2,0.4,0.25,0.1])

# school type
school_type = np.random.choice(["public", "private"], size=N, p=[0.4, 0.6])

# compute pass probability from features (sigmoid of a linear score)
# weights chosen to make pass ~65%
score = (
    0.06 * marks +
    0.08 * previous_marks / 100 * 100 +    # keep scale similar
    0.7 * (study_hours / 40) * 100 +        # scaled
    0.5 * (attendance) +
    1.5 * (assignments) +
    0.3 * extracurricular
)
# normalize
prob = 1 / (1 + np.exp(- (score - 90) / 10))  # shift/scale to get reasonable pass rates

# sample binary labels
result = (np.random.rand(N) < prob).astype(int)

# introduce label noise (~10% flips)
noise_idx = np.random.choice(N, size=int(0.10 * N), replace=False)
result[noise_idx] = 1 - result[noise_idx]

# assemble dataframe
df = pd.DataFrame({
    "student_id": student_id,
    "marks": marks,
    "study_hours_per_week": study_hours,
    "attendance_percent": attendance,
    "previous_year_marks": previous_marks,
    "assignments_submitted": assignments,
    "extracurricular_score": extracurricular,
    "parental_education_level": parent_edu,
    "school_type": school_type,
    "result": result
})

# save
df.to_csv("student_marks_dataset.csv", index=False)

# quick summary print
print("Saved student_marks_dataset.csv")
print(df.describe(include='all').transpose()[["count","mean","std","min","max"]].head(12))
print("\nClass distribution:\n", df['result'].value_counts(normalize=False).to_string())