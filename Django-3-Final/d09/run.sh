#!/usr/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate  --run-syncdb
python3 manage.py loaddata day.json
python3 manage.py runserver