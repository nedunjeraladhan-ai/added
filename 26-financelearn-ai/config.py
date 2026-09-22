import os
CHATBOT_TITLE='FinanceLearn AI'
DOMAIN='Financial Education'
SYSTEM_PROMPT='You are a specialized assistant for Financial Education. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to FinanceLearn AI. I can help you with Financial Education.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
