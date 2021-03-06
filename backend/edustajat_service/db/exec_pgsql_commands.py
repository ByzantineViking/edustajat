#!/usr/bin/python

import psycopg2
from edustajat_service.db.config import db_config
from edustajat_service.helpers.print import bcolors, section_print


def exec_pgsql_commands(commands):
    conn = None
    try:
        # read the connection parameters
        params = db_config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            # print(f"command: {command}")
            cur.execute(command)
        # close communication with the PostgreSQL database server
        section_print(bcolors.OKGREEN,
                      f"{len(commands)} sql command(s) executed succesfully", " OK")
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
