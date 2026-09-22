# ProjectPilot AI
**Domain:** Student Project Guidance

## Features
- Flask + Gemini server-side integration
- No login/register
- Temporary per-session chat history
- Domain-only responses
- Responsive UI
- Send, Enter-to-send, clear chat, typing indicator and error handling
- Render/Gunicorn compatible

## Local
`python -m venv venv`
`venv\\Scripts\\Activate.ps1`
`pip install -r requirements.txt`
Copy `.env.example` to `.env`, add `GEMINI_API_KEY`, then run `python app.py`.

Open `http://127.0.0.1:5000`.

## Render
Build: `pip install -r requirements.txt`
Start: `gunicorn app:app`
Add `GEMINI_API_KEY` and `FLASK_SECRET_KEY` in Render Environment Variables.
The app reads Render's `PORT` automatically.
