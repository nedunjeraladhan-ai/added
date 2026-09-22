import os
CHATBOT_TITLE='BusinessBasics AI'
DOMAIN='Business Fundamentals'
SYSTEM_PROMPT='You are a specialized assistant for Business Fundamentals. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to BusinessBasics AI. I can help you with Business Fundamentals.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
