import os
CHATBOT_TITLE='PresentationPro AI'
DOMAIN='Presentation Skills'
SYSTEM_PROMPT='You are a specialized assistant for Presentation Skills. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to PresentationPro AI. I can help you with Presentation Skills.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
