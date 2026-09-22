import os
CHATBOT_TITLE='ProjectPilot AI'
DOMAIN='Student Project Guidance'
SYSTEM_PROMPT='You are a specialized assistant for Student Project Guidance. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to ProjectPilot AI. I can help you with Student Project Guidance.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
