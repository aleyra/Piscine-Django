from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from d06.tools import ex_name, get_db_conn

# Create your views here.

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-insert/
# https://www.psycopg.org/psycopg3/docs/basic/params.html
# https://www.psycopg.org/psycopg3/docs/api/cursors.html#psycopg.AsyncCursor.fetchmany

movies = [
    {
        'episode_nb': 1,
        'title': 'The Phantom Menace',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '1999-05-19'
    },
    {
        'episode_nb': 2,
        'title': 'Attack of the Clones',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2002-05-16'
    },
    {
        'episode_nb': 3,
        'title': 'Revenge of the Sith',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2005-05-19'
    },
    {
        'episode_nb': 4,
        'title': 'A New Hope',
        'director': 'George Lucas',
        'producer': 'Gary Kurtz, Rick McCallum',
        'release_date': '1977-05-25'
    },
    {
        'episode_nb': 5,
        'title': 'The Empire Strikes Back',
        'director': 'Irvin Kershner',
        'producer': 'Gary Kutz, Rick McCallum',
        'release_date': '1980-05-17'
    },
    {
        'episode_nb': 6,
        'title': 'Return of the Jedi',
        'director': 'Richard Marquand',
        'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
        'release_date': '1983-05-25'
    },
    {
        'episode_nb': 7,
        'title': 'The Force Awakens',
        'director': 'J. J. Abrams',
        'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
        'release_date': '2015-12-11'
    }
]

def populate(request):
    ex_nb = ex_name(request)
    try:
        # connect to the PostgreSQL server
        conn = get_db_conn()
        cur = conn.cursor()

        command = f"""
            INSERT INTO {ex_nb}_movies(
                episode_nb,
                title,
                director,
                producer,
                release_date
            )
            VALUES (%s, %s, %s, %s, %s);
        """
        response = ""
        for movie in movies:
            try:
                cur.execute(command, (
                movie['episode_nb'],
                movie['title'],
                movie['director'],
                movie['producer'],
                movie['release_date']
                ))
                conn.commit()
                response += f"{movie['title']}: saved<br \>"
            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                response += f"{movie['title']}: {error}<br \>"
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(response)
    finally:
        if conn is not None:
            conn.close()
    return HttpResponse(response)

def display(request):
    ex_nb = ex_name(request)
    command = f"SELECT * from {ex_nb}_movies"

    try:
        # connect to the PostgreSQL server
        conn = get_db_conn()
        cur = conn.cursor()

        cur.execute(command)
        data = cur.fetchall()
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(f"No data available because: {error}")
    finally:
        if conn is not None:
            conn.close()

    return render(request, f"{ex_nb}/table.html", {'data': data})