import os
CHATBOT_TITLE='ExamBuddy AI'
DOMAIN='Exam Preparation'
SYSTEM_PROMPT='You are a specialized assistant for Exam Preparation. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to ExamBuddy AI. I can help you with Exam Preparation.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
