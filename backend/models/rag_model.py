import pinecone
from transformers import AutoTokenizer, AutoModel
import torch

class RAGModel:
    def __init__(self):
        pinecone.init(api_key='YOUR_API_KEY', environment='YOUR_ENVIRONMENT')
        self.index = pinecone.Index("your-index-name")
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = AutoModel.from_pretrained("distilbert-base-uncased")

    def index_course_document(self, course_data):
        # Tokenize and encode the document
        inputs = self.tokenizer(course_data['content'], return_tensors='pt')
        with torch.no_grad():
            embeddings = self.model(**inputs).last_hidden_state.mean(dim=1).numpy()

        # Add to Pinecone index
        self.index.upsert([(course_data['course_id'], embeddings.tolist())])

    def query(self, question):
        inputs = self.tokenizer(question, return_tensors='pt')
        with torch.no_grad():
            question_embedding = self.model(**inputs).last_hidden_state.mean(dim=1).numpy()

        # Search the index
        result = self.index.query(queries=question_embedding.tolist(), top_k=5)
        return result['matches']
