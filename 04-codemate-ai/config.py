import os
CHATBOT_TITLE='CodeMate AI'
DOMAIN='Programming'
SYSTEM_PROMPT='You are a specialized assistant for Programming. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to CodeMate AI. I can help you with Programming.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
