from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from ex00.views import params

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

    match request.path:
        case '/ex02/populate/':
            table_name = 'ex02_movies'
        case '/ex04/populate/':
            table_name = 'ex04_movies'

    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        

        command = f"""
            INSERT INTO {table_name}(
                episode_nb,
                title,
                director,
                producer,
                release_date
            )
            VALUES (%s, %s, %s, %s, %s);
        """
        for movie in movies:
            cur.execute(command, (
                movie['episode_nb'],
                movie['title'],
                movie['director'],
                movie['producer'],
                movie['release_date']
            ))
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

def display(request):
    match request.path:
        case '/ex02/display/':
            ex_name = 'ex02'
        case '/ex04/display/':
            ex_name = 'ex04'

    command = f"SELECT * from {ex_name}_movies"

    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command)
        data = cur.fetchall()
        # print(data)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(f"No data available because: {error}")
    finally:
        if conn is not None:
            conn.close()

    return render(request, f"{ex_name}/table.html", {'data': data})