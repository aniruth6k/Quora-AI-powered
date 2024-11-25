# Quid - AI-Powered Q&A Platform

Quid is an interactive Q&A platform leveraging AI to answer user-generated questions intelligently. This project combines a dynamic frontend with a Flask-based backend powered by a pre-trained natural language processing (NLP) model.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---


---

## Features

- **AI-Powered Responses:** Generates context-based answers using a pre-trained NLP model.
- **Dynamic Frontend:** Fetches and displays questions, answers, and categories dynamically.
- **User Interaction:** Allows users to ask questions and receive instant responses.
- **Easy Deployment:** Simple setup with Flask and vanilla JavaScript for quick deployment.
- **Extensible:** Modular code structure for easy enhancements and feature additions.

---

## Prerequisites

Before starting, ensure you have the following installed on your system:

- **Python 3.x**
- **Node.js** (optional, for future frontend enhancements)
- **pip** (Python package manager)

---

## Setup Instructions

### Backend Setup

Install dependencies:

pip install -r requirements.txt

Run the Flask server:

    python ai_backend.py

    The server will run on http://localhost:5000.

Frontend Setup

    Navigate to the frontend folder.

    Open index.html in your browser.

    Connect to the backend: Ensure the Flask server is running on http://localhost:5000.

Usage

    Open index.html in your browser.
    Use the input field to ask a question.
    Click "Submit" to receive an AI-generated response in an alert box.

Future Enhancements

    User Authentication: Implement user login and profiles to track contributions.
    Advanced NLP Models: Upgrade to more sophisticated models like GPT for richer responses.
    React Frontend: Replace the static frontend with a React-based dynamic UI.
    Database Integration: Store user questions, answers, and feedback in a database.
    Analytics Dashboard: Add insights and metrics about user engagement and question trends.

Contributing

We welcome contributions! To contribute:

    Fork this repository.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -m "Add feature").
    Push to the branch (git push origin feature-branch).
    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.


