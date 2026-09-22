import os
CHATBOT_TITLE='MathMind AI'
DOMAIN='Mathematics'
SYSTEM_PROMPT='You are a specialized assistant for Mathematics. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to MathMind AI. I can help you with Mathematics.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
