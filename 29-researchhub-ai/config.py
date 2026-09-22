import os
CHATBOT_TITLE='ResearchHub AI'
DOMAIN='Academic Research'
SYSTEM_PROMPT='You are a specialized assistant for Academic Research. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to ResearchHub AI. I can help you with Academic Research.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
