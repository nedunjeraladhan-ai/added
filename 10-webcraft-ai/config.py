import os
CHATBOT_TITLE='WebCraft AI'
DOMAIN='Web Development'
SYSTEM_PROMPT='You are a specialized assistant for Web Development. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to WebCraft AI. I can help you with Web Development.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
