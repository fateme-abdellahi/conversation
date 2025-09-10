# groq

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
   cd groq
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   ```

   On windows
   ```sh
   venv\Scripts\activate  # Windows
   ```

   On linux
   ```sh
   source venv\bin\activate  # Linux
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in `groq/groq-api` with:
   ```
   DEBUG=True
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1

   # PostgreSQL settings
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=groq_db
   DB_USER=postgres
   DB_PASSWORD=your_db_password
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

All endpoints are under `/api/`:

- `POST /api/register/`  
  Register a new user.  
  **Body:** `{ "username": "yourname", "password": "yourpassword" }`

- `POST /api/login/`  
  Login and receive JWT tokens.  
  **Body:** `{ "username": "yourname", "password": "yourpassword" }`  
  **Response:** `{ "refresh": "...", "access": "..." }`

- `POST /api/conversation/`  
  Send a message to Groq API (JWT required).  
  **Body:** `{ "message": "your message" }`  
  **Response:** `{ "response": "model response" }`

## Authentication

- Use the `access` token from `/api/login/` in the `Authorization` header:
  ```
  Authorization: Bearer <access_token>
  ```

## Environment Variables

- All sensitive data (API keys, DB credentials) are managed via `.env` file.

## License

[MIT License](./LICENSE)