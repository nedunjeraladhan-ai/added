import os
CHATBOT_TITLE='DBMaster AI'
DOMAIN='Database Management'
SYSTEM_PROMPT='You are a specialized assistant for Database Management. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to DBMaster AI. I can help you with Database Management.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
