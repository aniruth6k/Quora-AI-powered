// Fetch and display questions
async function fetchQuestions() {
    const response = await fetch('/api/questions');
    const questions = await response.json();
    const container = document.getElementById('questions-container');
    container.innerHTML = questions.map(q => `<p>${q}</p>`).join('');
}

// Submit a question and fetch AI response
async function submitQuestion() {
    const question = document.getElementById('question-input').value;
    const response = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    });
    const data = await response.json();
    alert(`AI Response: ${data.answer}`);
}

// Initial fetch
fetchQuestions();
