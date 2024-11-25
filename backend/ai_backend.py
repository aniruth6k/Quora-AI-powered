from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a simple language model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Sample data for questions
questions_data = [
    "What is Quid?",
    "How does AI work in Quid?",
    "What are popular categories in Quid?"
]

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(questions_data)

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    context = "Quid is an AI-powered Q&A platform designed to answer user questions intelligently. It uses machine learning models to provide accurate responses."
    answer = qa_pipeline(question=question, context=context)
    return jsonify({'answer': answer['answer']})

if __name__ == '__main__':
    app.run(debug=True)
