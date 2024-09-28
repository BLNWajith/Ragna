from transformers import pipeline

# Initialize the text generation pipeline with a pre-trained model
generator = pipeline("text-generation", model="gpt-4")

def generate_course_content(topic):
    prompt = f"Write a detailed overview of {topic}, including its applications and prerequisites."
    response = generator(prompt, max_length=500)
    return response[0]['generated_text']

def generate_faqs(topic):
    prompt = f"Generate 5 common questions and answers related to {topic}."
    response = generator(prompt, max_length=500)
    return response[0]['generated_text']