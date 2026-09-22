import os
CHATBOT_TITLE='QuizCraft AI'
DOMAIN='Quiz and Exam Practice'
SYSTEM_PROMPT='You are a specialized assistant for Quiz and Exam Practice. Stay strictly within this domain and provide clear, useful answers.'
WELCOME_MESSAGE='Welcome to QuizCraft AI. I can help you with Quiz and Exam Practice.'
MAX_HISTORY_MESSAGES=12
SECRET_KEY=os.getenv("FLASK_SECRET_KEY","change-this-secret-in-production")
PORT=int(os.getenv("PORT","5000"))
