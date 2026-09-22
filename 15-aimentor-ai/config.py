import os
CHATBOT_TITLE='AIMentor AI'
DOMAIN='Artificial Intelligence'
SYSTEM_PROMPT='You are a specialized assistant for Artificial Intelligence. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to AIMentor AI. I can help you with Artificial Intelligence.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
