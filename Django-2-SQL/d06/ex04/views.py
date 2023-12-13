from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import psycopg2

from .form import RemoveForm
from d06.tools import ex_name, get_db_conn

# Create your views here.

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-delete/
def remove(request):
    ex_nb = ex_name(request)

    # get_cmd = f"""
    #     SELECT title FROM {ex_name}_movies
    # """  # pas reussi
    get_cmd = f"""
        SELECT * FROM {ex_nb}_movies;
    """  # pas reussi

    # get titles
    try:
        # connect to the PostgreSQL server
        conn = get_db_conn()
        cur = conn.cursor()
        
        cur.execute(get_cmd)
        table = cur.fetchall()  # [('The Phantom Menace',), ... , ('The Force Awakens',)]
        # print(table)  #
    except (Exception, psycopg2.DatabaseError) as error:
        return HttpResponse(f"No data available because: {error}")
    
    # display titles
    if (request.method == "GET"):
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        # print(f"\n\n{table}\n\n")  #
        context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in table))}
        if len(table) == 0:
            return HttpResponse("No data available")
        return render(request, f"{ex_nb}/remove.html", context)

    # delete selected title
    elif (request.method == "POST"):
        title_delete = request.POST.get('title')
        delete_cmd = f"""
            DELETE FROM {ex_nb}_movies
            WHERE title = '{title_delete}';
        """
        try:
            cur.execute(delete_cmd)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            return HttpResponse(f"Fail to remove: {error}")

        finally:
            if conn is not None:
                conn.close()
    return HttpResponseRedirect(request.path)