import os
CHATBOT_TITLE='CampusMate AI'
DOMAIN='College Information'
SYSTEM_PROMPT='You are a specialized assistant for College Information. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to CampusMate AI. I can help you with College Information.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
