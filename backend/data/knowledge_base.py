import json

def save_course_content(course_data, filename='courses.json'):
    with open(filename, 'w') as f:
        json.dump(course_data, f)

def save_faqs(faqs, filename='faqs.json'):
    with open(filename, 'w') as f:
        json.dump(faqs, f)

# Example functions to create and save structured content
def create_course_data(course_id, title, content, prerequisites, learning_objectives, tags):
    return {
        "course_id": course_id,
        "title": title,
        "content": content,
        "prerequisites": prerequisites,
        "learning_objectives": learning_objectives,
        "tags": tags
    }

def create_faq_data(course_id, faqs):
    return {
        "course_id": course_id,
        "faqs": faqs
    }