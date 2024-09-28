# backend/utils/uncertainty.py

import torch
from scipy.stats import entropy

def calculate_entropy_uncertainty(output_probs):
    """
    Calculates uncertainty using entropy for the given output probabilities.

    Args:
        output_probs (torch.Tensor): Output probabilities from the model (shape: [batch_size, num_classes]).

    Returns:
        float: The entropy-based uncertainty.
    """
    return entropy(output_probs.detach().numpy())

def calculate_quantile_regression_forests(model, X):
    """
    Calculates uncertainty using Quantile Regression Forests.

    Args:
        model (sklearn.ensemble.QuantileRegressionForest): Trained Quantile Regression Forest model.
        X (pd.DataFrame): Input features for which to calculate uncertainty.

    Returns:
        np.ndarray: The uncertainty estimates for each sample in X.
    """
    pass