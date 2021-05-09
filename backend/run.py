from dotenv import load_dotenv
load_dotenv()  # by default, doesn't override any existing environment variables


import os
from edustajat_service.db.connect import connect
from edustajat_service.refine_data import ehdokkaat, tulokset_ehdokkaittain


def init_ehdokkaat_db(conn):
    """ Run locally and then use heroku to update database, see README """
    ehdokkaat.run(conn)
    tulokset_ehdokkaittain.run(conn)


if __name__ == '__main__':
    conn = connect()
