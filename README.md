# conversation

A Django REST API for conversational AI using Groq's external API, with JWT authentication and PostgreSQL support.

## Features

- User registration and login with JWT authentication
- Secure endpoints for conversation with Groq API
- Stores user messages and model responses in PostgreSQL

## Requirements

- Python 3.11+
- Django 5.2.6
- djangorestframework
- djangorestframework-simplejwt
- psycopg2
- groq
- python-dotenv

## Setup

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd conversation
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   ```

   On Windows
   ```sh
   venv\Scripts\activate
   ```

   On Linux
   ```sh
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in `conversation/conversation` with:
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1

   # PostgreSQL settings
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=your_database
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=5432

   # Groq API
   GROQ_API_KEY=your_groq_api_key
   GROQ_URL=https://api.groq.com/openai/v1/chat/completions
   GROQ_MODEL=meta-llama/llama-4-scout-17b-16e-instruct
   ```

5. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

6. **Run the server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- `POST /auth/register/`  
  Register a new user.  
  **Body:** `{ "username": "yourname", "password": "yourpassword" }`

- `POST /auth/login/`  
  Login and receive JWT tokens.  
  **Body:** `{ "username": "yourname", "password": "yourpassword" }`  
  **Response:** `{ "refresh": "...", "access": "..." }`

- `POST /api/conversation/`  
  Send a message to Groq API (JWT required).  
  **Body:** `{ "message": "your message" }`  
  **Response:** `{ "response": "model response" }`

## Authentication

- Use the `access` token from `/auth/login/` in the `Authorization` header:
  ```
  Authorization: Bearer <access_token>
  ```

## License

[MIT License](./LICENSE)