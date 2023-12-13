from . import settings
import psycopg2


def get_db_conn():
	param = settings.DATABASES["default"]
	return psycopg2.connect(f"\
						dbname={param['NAME']}\
						user={param['USER']}\
						password={param['PASSWORD']}\
						host={param['HOST']}\
						port={param['PORT']}")


def ex_name(request):
	parse = request.path.split('/')
	if (len(parse) < 2): raise Exception(f"not know {request.path}")
	return(f"{parse[1]}")