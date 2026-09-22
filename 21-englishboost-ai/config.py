import os
CHATBOT_TITLE='EnglishBoost AI'
DOMAIN='English Learning'
SYSTEM_PROMPT='You are a specialized assistant for English Learning. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to EnglishBoost AI. I can help you with English Learning.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
