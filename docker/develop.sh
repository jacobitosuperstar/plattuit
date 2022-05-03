#!/bin/sh

# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

# Develop service
# echo 'Iniciando servidor'
# python3 manage.py runserver 0.0.0.0:8000

# Probando el servicio sincrónico
# pipenv run gunicorn website.wsgi:application --bind 0.0.0.0:8000

# Probrando el servicio asincónico
# pipenv run daphne -b 0.0.0.0 -p 8000 website.asgi:application

sleep 15
echo 'Iniciando las pruebas'
python3 manage.py test interaction
