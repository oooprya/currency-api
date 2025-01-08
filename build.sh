#!/usr/bin/env bash
# exit on error

python manage.py collectstatic --no-input
# python manage.py migrate
python manage.py makemigrations
python manage.py migrate
