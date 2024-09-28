import chromadb

class ChromaDBConnector:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name="courses")

    def insert_document(self, document_id, content, metadata):
        self.collection.add(id=document_id, content=content, metadata=metadata)

    def find_documents(self, query, top_k=5):
        results = self.collection.query(content=query, n_results=top_k)
        return results

    def delete_document(self, document_id):
        self.collection.delete(id=document_id)