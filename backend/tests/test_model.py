# backend/tests/test_models.py

import pytest
from backend.models.ensemble_model import EnsembleModel
from backend.models.llm_model import LLMModel
from backend.models.rag_model import RAGModel
from backend.database.pinecone_connector import MongoDBConnector

@pytest.fixture
def ensemble_model():
    db_connector = MongoDBConnector()
    llm_model = LLMModel()
    rag_model = RAGModel(db_connector)
    return EnsembleModel(llm_model, rag_model)

def test_ensemble_model_recommendation(ensemble_model):
    user_profile = {
        "id": 1,
        "name": "John Doe",
        "age": 20,
        "education": "high school"
    }
    user_progress = {
        "Course 1": 80,
        "Course 2": 60
    }
    query = "What course should I take next?"

    recommendation = ensemble_model.get_recommendation(user_profile, user_progress, query)

    assert "recommendation" in recommendation
    assert "llm_uncertainty" in recommendation
    assert "rag_uncertainty" in recommendation
    assert "llm_shap_values" in recommendation
    assert "rag_shap_values" in recommendation

