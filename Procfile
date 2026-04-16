release: python manage.py migrate && python seed_users.py
web: gunicorn Project.wsgi