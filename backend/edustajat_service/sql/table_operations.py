from edustajat_service.db.exec_pgsql_commands import exec_pgsql_commands
from edustajat_service.sql.helpers.execute_sql_file import execute_sql_file
import psycopg2
from psycopg2.extras import execute_values
from io import StringIO
from edustajat_service.helpers.print import bcolors, section_print


def create_tables():
    """ create tables in the PostgreSQL database"""
    execute_sql_file("./sql/create_tables.sql")


def bulk_insert_stringio(conn, df, table):
    """
    Using psycopg2.extras.execute_values() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        print(f"Starting bulk insert into table \"{table}\"")
        execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        section_print(bcolors.FAIL, "Bulk insert status", "ERROR")
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    section_print(bcolors.OKGREEN, "Bulk insert status", "OK")
    cursor.close()
