import random
import math
import pandas as pd
import numpy as np
def create_records(n):
    student_info = []
    i = 1
    while i <= n:
        marks = random.randint(0, 100)
        attend = random.randint(0, 100)
        assign = random.randint(0, 50)
        perf_index = (marks * 0.6 + assign * 0.4) * math.log(attend + 1)
        student_info.append((i, marks, attend, assign, perf_index))
        i += 1
    return student_info
def categorize_students(student_info):
    categories = {}
    for entry in student_info:
        sid, marks, attend, assign, perf_index = entry
        if marks < 40 or attend < 50:
            categories[sid] = "At Risk"
        elif marks > 90 and attend > 80:
            categories[sid] = "Top Performer"
        elif marks >= 70:
            categories[sid] = "Good"
        else:
            categories[sid] = "Average"
    return categories
def evaluate_data(student_info, categories):
    df = pd.DataFrame(student_info, columns=["ID", "Marks", "Attendance", "Assignment", "PI"])
    marks_list = df["Marks"].values
    total_marks = sum(marks_list)
    mean_val = total_marks / len(marks_list)

    median_val = np.median(marks_list)
    std_dev = np.std(marks_list)
    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]
    min_val = np.min(marks_list)
    max_val = np.max(marks_list)
    df["Normalized"] = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in marks_list]
    category_set = set(categories.values())
    low_attendance = sum(1 for v in df["Attendance"] if v < 50)
    high_marks = sum(1 for v in df["Marks"] if v > 90)
    consistent = std_dev < 15
    if consistent and low_attendance <= 3:
        result = "Stable Academic System"
    elif high_marks >= 2:
        result = "Moderate Performance"
    else:
        result = "Critical Attention Required"

    summary_tuple = (mean_val, std_dev, max_val)
    return df, median_val, correlation, summary_tuple, result, category_set
roll_number = "AP24110011589"
last_digit = int(roll_number[-1])
n = last_digit
student_info = create_records(n)
categories = categorize_students(student_info)
df, median_val, correlation, summary_tuple, result, category_set = evaluate_data(student_info, categories)
print(df)
print(categories)
print(category_set)
print(median_val)
print(correlation)
print(summary_tuple)
print(result)
