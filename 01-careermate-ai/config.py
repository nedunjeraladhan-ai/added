import os
CHATBOT_TITLE='CareerMate AI'
DOMAIN='Career Guidance'
SYSTEM_PROMPT='You are a specialized assistant for Career Guidance. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to CareerMate AI. I can help you with Career Guidance.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
