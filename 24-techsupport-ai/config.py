import os
CHATBOT_TITLE='TechSupport AI'
DOMAIN='Technology Support'
SYSTEM_PROMPT='You are a specialized assistant for Technology Support. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to TechSupport AI. I can help you with Technology Support.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
