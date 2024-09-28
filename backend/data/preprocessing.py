# backend/data/preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data):
        """
        Preprocesses the input data by handling missing values, encoding categorical variables,
        and scaling numerical features.

        Parameters:
        data (pd.DataFrame): The input data to preprocess.

        Returns:
        pd.DataFrame: The preprocessed data.
        """
        # Handle missing values
        data = data.fillna(data.mean())

        # Encode categorical variables
        data = pd.get_dummies(data)

        # Scale numerical features
        numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
        data[numerical_columns] = self.scaler.fit_transform(data[numerical_columns])

        return data

    def split_data(self, data, target_column, test_size=0.2):
        """
        Splits the data into training and testing sets.

        Parameters:
        data (pd.DataFrame): The input data to split.
        target_column (str): The name of the target column.
        test_size (float): The proportion of the dataset to include in the test split.

        Returns:
        tuple: The training and testing sets.
        """
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)