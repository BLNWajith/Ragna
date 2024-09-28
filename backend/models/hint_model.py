# backend/models/hint_model.py

from transformers import AutoModelForCausalLM, AutoTokenizer

class HintModel:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_hint(self, question):
        inputs = self.tokenizer.encode(question, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=50, num_return_sequences=1)
        hint = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return hint.strip()
