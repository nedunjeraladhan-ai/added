import os
CHATBOT_TITLE='DesignDesk AI'
DOMAIN='UI/UX Design'
SYSTEM_PROMPT='You are a specialized assistant for UI/UX Design. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to DesignDesk AI. I can help you with UI/UX Design.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
