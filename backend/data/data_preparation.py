# backend/data/data_preparation.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_and_prepare_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"
    df = pd.read_csv(url, sep=';')

    courses = pd.DataFrame({
        'course_id': range(1, 11),
        'course_name': [f'Course {i}' for i in range(1, 11)],
        'difficulty': np.random.choice(['Easy', 'Medium', 'Hard'], 10),
        'duration_weeks': np.random.randint(4, 13, 10)
    })

    enrollments = []
    for _, student in df.iterrows():
        num_courses = np.random.randint(1, 5)
        for _ in range(num_courses):
            course = courses.sample(1).iloc[0]
            enrollments.append({
                'student_id': student.name,
                'course_id': course['course_id'],
                'progress': np.random.randint(0, 101),
                'grade': np.random.randint(0, 21)
            })
    enrollments_df = pd.DataFrame(enrollments)
    merged_data = pd.merge(df, enrollments_df, left_index=True, right_on='student_id')
    merged_data = pd.merge(merged_data, courses, on='course_id')
    train_data, test_data = train_test_split(merged_data, test_size=0.2, random_state=42)
    return train_data, test_data, courses

train_data, test_data, courses = load_and_prepare_data()