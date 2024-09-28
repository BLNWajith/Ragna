# backend/utils/explainability.py

from shap import Explainer

def get_shap_explanations(model, tokenizer, prompt):
    """
    Calculates SHAP values for the given model and prompt.

    Args:
        model (transformers.AutoModelForCausalLM): The LLM model.
        tokenizer (transformers.AutoTokenizer): The tokenizer for the model.
        prompt (str): The input prompt.

    Returns:
        np.ndarray: The SHAP values for each token in the prompt.
    """
    explainer = Explainer(model)
    encoded_prompt = tokenizer.encode(prompt, return_tensors="pt")
    return explainer.shap_values(encoded_prompt)