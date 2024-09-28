# backend/data/active_learning.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss

class ActiveLearner:
    def __init__(self, model=None, num_samples_to_label=5):
        self.model = model if model else RandomForestClassifier(n_estimators=100, random_state=42)
        self.num_samples_to_label = num_samples_to_label

    def fit(self, X, y):
        """
        Trains the model on the provided data.

        Parameters:
        X (pd.DataFrame): The input features.
        y (pd.Series): The target labels.
        """
        self.model.fit(X, y)

    def predict_proba(self, X):
        """
        Predicts the probabilities for the input features.

        Parameters:
        X (pd.DataFrame): The input features.

        Returns:
        np.ndarray: The predicted probabilities.
        """
        return self.model.predict_proba(X)

    def select_samples_to_label(self, X_pool, y_pool=None):
        """
        Selects the most informative samples for labeling using an uncertainty-based approach.

        Parameters:
        X_pool (pd.DataFrame): The pool of unlabeled samples.
        y_pool (pd.Series): The pool of unlabeled targets (optional).

        Returns:
        pd.DataFrame: The selected samples for labeling.
        """
        if y_pool is not None:
            self.fit(X_pool, y_pool)
        probabilities = self.predict_proba(X_pool)
        entropy = -np.sum(probabilities * np.log(probabilities + 1e-9), axis=1)
        selected_indices = np.argsort(entropy)[-self.num_samples_to_label:]
        selected_samples = X_pool.iloc[selected_indices]
        return selected_samples

    def update_model(self, X_new, y_new):
        """
        Updates the model with newly labeled samples.

        Parameters:
        X_new (pd.DataFrame): The new input features.
        y_new (pd.Series): The new target labels.
        """
        self.model.fit(X_new, y_new)