from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.models.rag_model import RAGModel
from backend.data.course_content_generator import generate_course_content, generate_faqs
from backend.data.knowledge_base import save_course_content, save_faqs, create_course_data, create_faq_data
from backend.utils.hint_generation import get_hint

app = FastAPI()
rag_model = RAGModel()

class CourseContent(BaseModel):
    course_id: str
    title: str
    content: str
    prerequisites: list
    learning_objectives: list
    tags: list

@app.post("/courses/add")
def add_course_content(content: CourseContent):
    course_data = create_course_data(
        course_id=content.course_id,
        title=content.title,
        content=content.content,
        prerequisites=content.prerequisites,
        learning_objectives=content.learning_objectives,
        tags=content.tags
    )
    rag_model.index_course_document(course_data)
    save_course_content(course_data)
    return {"status": "success"}

@app.post("/faqs/add")
def add_faqs(course_id: str):
    faqs = generate_faqs(course_id)  # Using the topic as course_id for demo
    faq_data = create_faq_data(course_id, faqs)
    save_faqs(faq_data)
    return {"status": "success", "faqs": faqs}

@app.get("/courses/query")
def query_course(question: str):
    answer = rag_model.query(question)
    return answer


class HintRequest(BaseModel):
    question: str

@app.post("/get_hint")
def fetch_hint(request: HintRequest):
    if not request.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    hint = get_hint(request.question)
    return {"hint": hint}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)