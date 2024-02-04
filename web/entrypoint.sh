#!/bin/sh

python manage.py makemigrations
python manage.py migrate
# Start your Django application (replace 'gunicorn' with your preferred application server)
exec gunicorn hobbyHunter.wsgi:application -w 2 -b :8000
