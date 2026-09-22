import os
CHATBOT_TITLE='ResumePro AI'
DOMAIN='Resume and Career Documents'
SYSTEM_PROMPT='You are a specialized assistant for Resume and Career Documents. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to ResumePro AI. I can help you with Resume and Career Documents.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
