# User Interaction Tracker

A full-featured Django backend project that integrates:

- Django REST Framework (DRF)
- JWT Authentication
- Celery + Redis for async tasks
- Telegram Bot integration
- Environment variable management

---

## 🚀 Features

- User registration and JWT login
- Protected and public API endpoints
- Welcome email via Celery on signup
- Telegram Bot `/start`, `/profile`, `/help`, `/dashboard` commands
- Telegram-Django integration for sending messages

---

## 🛠️ Setup Instructions

1. ## Clone the Repository**
bash
git clone https://github.com/piyushguptaofficial/user-interaction-tracker.git
cd user-interaction-tracker

2. ## CREATE VIRTUAL ENVIRONMENT
python -m venv venv
source venv/bin/activate  ||  Windows: venv\\Scripts\\activate

3. ## INSTALL DEPENDENCIES
- pip install -r requirements.txt


4. ## SET UP .env FILE
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
TELEGRAM_BOT_TOKEN=your-telegram-token
CELERY_BROKER_URL=redis://localhost:6379/0

5. ## RUN REDIS IN WSL
sudo service redis-server start

6. ## RUN MIGRATIONS & SERVER
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

7. ## START CELERY WORKER
celery -A config worker --loglevel=info

8. ## START TELEGRAM BOT
python telegram_bot.py



## API ROUTES ##

| Method | Route                 | Description               |
| ------ | --------------------- | ------------------------- |
| GET    | `/api/public/`        | Public welcome route      |
| POST   | `/api/register/`      | Register new user         |
| POST   | `/api/token/`         | Login, get JWT token      |
| POST   | `/api/token/refresh/` | Refresh JWT token         |
| GET    | `/api/dashboard/`     | Protected, requires token |


