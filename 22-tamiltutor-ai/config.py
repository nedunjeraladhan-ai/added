import os
CHATBOT_TITLE='TamilTutor AI'
DOMAIN='Tamil Language Learning'
SYSTEM_PROMPT='You are a specialized assistant for Tamil Language Learning. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to TamilTutor AI. I can help you with Tamil Language Learning.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
