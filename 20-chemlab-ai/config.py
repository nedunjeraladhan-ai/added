import os
CHATBOT_TITLE='ChemLab AI'
DOMAIN='Chemistry'
SYSTEM_PROMPT='You are a specialized assistant for Chemistry. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to ChemLab AI. I can help you with Chemistry.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
