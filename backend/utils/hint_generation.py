# backend/utils/hint_generation.py

from backend.models.hint_model import HintModel

def get_hint(question):
    hint_model = HintModel()
    hint = hint_model.generate_hint(question)
    return hint
