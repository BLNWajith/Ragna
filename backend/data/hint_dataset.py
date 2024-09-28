# backend/data/hint_dataset.py

import pandas as pd

# Sample data for training the hint-generating model
data = {
    "questions": [
        "What is the definition of machine learning?",
        "How does a decision tree work?",
        "What are the prerequisites for learning deep learning?",
        "Explain the concept of overfitting.",
        "What is the difference between supervised and unsupervised learning?"
    ],
    "hints": [
        "Think about algorithms that learn from data.",
        "Consider how the tree splits based on feature values.",
        "What foundational topics in mathematics are important?",
        "What happens when the model learns too well?",
        "How do labels in datasets affect the learning process?"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv("backend/data/hint_dataset.csv", index=False)
