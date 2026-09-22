import os
CHATBOT_TITLE='DigitalSkills AI'
DOMAIN='Digital Skills'
SYSTEM_PROMPT='You are a specialized assistant for Digital Skills. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to DigitalSkills AI. I can help you with Digital Skills.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
