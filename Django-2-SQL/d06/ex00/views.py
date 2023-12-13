from django.http import HttpResponse
import psycopg2
from d06 import settings

# https://www.postgresqltutorial.com/postgresql-python/create-tables/
# https://www.psycopg.org/docs/module.html
# https://www.postgresql.org/docs/16/ddl-constraints.html
# https://www.postgresql.org/docs/16/datatype.html

params = {
    'dbname': settings.DATABASES['default']['NAME'],
    'user': settings.DATABASES['default']['USER'],
    'password': settings.DATABASES['default']['PASSWORD'],
    'host': settings.DATABASES['default']['HOST'],
    'port': settings.DATABASES['default']['PORT'],
}

# Create your views here.
def init(request):

    match request.path:
        case '/ex00/init/':
            table_name = 'ex00_movies'
        case '/ex02/init/':
            table_name = 'ex02_movies'
        case '/ex04/init/':
            table_name = 'ex04_movies'

    commands = [
        f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
            title VARCHAR(64) NOT NULL UNIQUE,
            episode_nb INTEGER PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
    ]

    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(error)
    finally:
        if conn is not None:
            conn.close()
    return HttpResponse("OK")
