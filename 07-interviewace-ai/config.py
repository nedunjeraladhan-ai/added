import os
CHATBOT_TITLE='InterviewAce AI'
DOMAIN='Interview Preparation'
SYSTEM_PROMPT='You are a specialized assistant for Interview Preparation. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to InterviewAce AI. I can help you with Interview Preparation.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
