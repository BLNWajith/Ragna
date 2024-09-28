# backend/models/ensemble_model.py

# backend/models/ensemble_model.py

from backend.models.llm_model import LLMModel
from backend.models.rag_model import RAGModel

class EnsembleModel:
    def __init__(self, llm_model: LLMModel, rag_model: RAGModel):
        self.llm_model = llm_model
        self.rag_model = rag_model

    def get_recommendation(self, user_profile, user_progress, query):
        # Get information from the RAG model
        rag_output = self.rag_model.query_knowledge_base(query)
        
        # Get LLM response
        llm_output = self.llm_model.generate_response(query)
        
        # Combine outputs
        recommendation = {
            "recommendation": llm_output,
            "rag_info": rag_output,
            "llm_uncertainty": self.llm_model.calculate_uncertainty(),
            "rag_uncertainty": self.rag_model.calculate_uncertainty(),
            "llm_shap_values": self.llm_model.get_shap_values(query),
            "rag_shap_values": self.rag_model.get_shap_values(query),
        }
        return recommendation
