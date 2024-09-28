# backend/models/llm_model.py

from transformers import AutoModelForCausalLM, AutoTokenizer
from torch import nn
import torch
from scipy.stats import entropy
from shap import Explainer

from config import LLM_MODEL_NAME, LLM_MAX_LENGTH

class LLMModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(LLM_MODEL_NAME)
        self.explainer = Explainer(self.model)

    def generate_response(self, prompt, user_profile=None, max_length=LLM_MAX_LENGTH):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1)
        response = self.tokenizer.decode(outputs, skip_special_tokens=True)

        output_probs = torch.nn.functional.softmax(self.model(input_ids=inputs).logits, dim=-1)
        uncertainty = entropy(output_probs.detach().numpy())

        shap_values = self.explainer.shap_values(self.tokenizer.encode(prompt, return_tensors="pt"))
        explanation = {
            "response": response,
            "uncertainty": uncertainty,
            "shap_values": shap_values
        }

        return explanation

    def fine_tune(self, dataset):
        pass