# backend/models/probabilistic_model.py

from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
from backend.utils.uncertainty import calculate_entropy_uncertainty

class ProbabilisticModel:
    def __init__(self, model_structure):
        """
        Initialize the Bayesian Model.

        Args:
            model_structure (list of tuples): Structure of the Bayesian model (e.g., [('A', 'C'), ('B', 'C')]).
        """
        self.model = BayesianModel(model_structure)
        self.inference = VariableElimination(self.model)

    def train(self, data):
        """
        Train the model on the provided data.

        Args:
            data (pd.DataFrame): The training data.
        """
        self.model.fit(data)

    def predict(self, input_features):
        """
        Predict based on input features.

        Args:
            input_features (dict): The features for which predictions are to be made.

        Returns:
            dict: Predictions based on the input features.
        """
        return self.inference.query(variables=input_features.keys(), evidence=input_features)

    def calculate_uncertainty(self, predictions):
        """
        Calculate uncertainty based on predictions.

        Args:
            predictions (dict): Predictions made by the model.

        Returns:
            float: Entropy-based uncertainty.
        """
        return calculate_entropy_uncertainty(predictions)
