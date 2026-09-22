import os
CHATBOT_TITLE='CloudGuide AI'
DOMAIN='Cloud Computing'
SYSTEM_PROMPT='You are a specialized assistant for Cloud Computing. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to CloudGuide AI. I can help you with Cloud Computing.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
