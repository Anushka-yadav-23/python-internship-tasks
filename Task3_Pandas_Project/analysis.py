# ==========================================
# Task 3 - Pandas Data Analysis Project
# Student Performance Analysis
# ==========================================

import pandas as pd

try:
    # Load dataset
    df = pd.read_csv("students.csv")

    print("\n===== ORIGINAL DATA =====")
    print(df)

    # Check missing values
    print("\n===== MISSING VALUES CHECK =====")
    print(df.isnull().sum())

    # Data Cleaning (if any missing values)
    df = df.fillna(0)

    # Calculate Average Score
    df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

    # Filter: Students with average > 70
    top_students = df[df["Average"] > 70]

    # Grouping (basic insight)
    avg_subject_scores = df[["Math", "Science", "English"]].mean()

    print("\n===== TOP STUDENTS (Average > 70) =====")
    print(top_students)

    print("\n===== SUBJECT-WISE AVERAGE =====")
    print(avg_subject_scores)

    # Attendance insight
    high_attendance = df[df["Attendance"] >= 90]

    print("\n===== HIGH ATTENDANCE STUDENTS =====")
    print(high_attendance)

    # Save processed data
    df.to_csv("processed_students.csv", index=False)

    print("\nProcessed data saved to processed_students.csv")

except FileNotFoundError:
    print("Error: students.csv file not found.")

except Exception as e:
    print("Unexpected Error:", e)
    