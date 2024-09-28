# source code from CHATGPT-3.5
import csv
import random
import string

# Define the number of rows
rows = 1000

# Function to generate random data
def generate_random_course_name():
    adjectives = ["Introduction", "Advanced", "Intermediate", "Basic"]
    subjects = ["Python", "Data Science", "Machine Learning", "Statistics"]
    return f"{random.choice(adjectives)} {random.choice(subjects)}"

def generate_random_topic_name():
    topics = ["Variables and Data Types", "Control Structures", "Functions", "Pandas and NumPy", "Linear Regression"]
    return random.choice(topics)

def generate_random_user_id():
    return random.randint(1, 1000)

def generate_random_course_id():
    return random.randint(1, 100)

def generate_random_topic_id():
    return random.randint(1, 50)

def generate_random_progress():
    return round(random.uniform(0.0, 1.0), 2)

# Generate the data
data = [
    {
        'user_id': generate_random_user_id(),
        'course_id': generate_random_course_id(),
        'course_name': generate_random_course_name(),
        'topic_id': generate_random_topic_id(),
        'topic_name': generate_random_topic_name(),
        'progress': generate_random_progress()
    } for _ in range(rows)
]

# Write the data to a CSV file
with open('learning_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['user_id', 'course_id', 'course_name', 'topic_id', 'topic_name', 'progress']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Generated {rows} rows of data and saved to learning_data.csv")
