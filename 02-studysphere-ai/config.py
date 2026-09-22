import os
CHATBOT_TITLE='StudySphere AI'
DOMAIN='Study and Learning'
SYSTEM_PROMPT='You are a specialized assistant for Study and Learning. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to StudySphere AI. I can help you with Study and Learning.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
