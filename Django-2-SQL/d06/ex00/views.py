from django.http import HttpResponse
import psycopg2
from d06.tools import ex_name, get_db_conn

# https://www.postgresqltutorial.com/postgresql-python/create-tables/
# https://www.psycopg.org/docs/module.html
# https://www.postgresql.org/docs/16/ddl-constraints.html
# https://www.postgresql.org/docs/16/datatype.html

# Create your views here.
def init(request):

    ex_nb = ex_name(request)
    print(ex_nb)

    commands = [
        f"""
        CREATE TABLE IF NOT EXISTS {ex_nb}_movies(
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
        conn = get_db_conn()
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
