from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

from ex00.views import params

# Create your views here.

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-delete/
def remove(request):
    match request.path:
        case '/ex02/remove/':
            ex_name = 'ex02'
        case '/ex03/remove/':
            ex_name = 'ex03'
        case '/ex04/remove/':
            ex_name = 'ex04'

    command = f"""
        DELETE FROM {ex_name}_movies
        WHERE title = %s
    """

    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()