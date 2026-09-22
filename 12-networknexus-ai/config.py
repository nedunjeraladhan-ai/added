import os
CHATBOT_TITLE='NetworkNexus AI'
DOMAIN='Computer Networks'
SYSTEM_PROMPT='You are a specialized assistant for Computer Networks. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to NetworkNexus AI. I can help you with Computer Networks.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
