from edustajat_service.db.exec_pgsql_commands import exec_pgsql_commands
from edustajat_service.sql.helpers.execute_sql_file import execute_scripts_from_file
import psycopg2
from psycopg2.extras import execute_values


def create_tables():
    """ create tables in the PostgreSQL database"""
    execute_scripts_from_file("./sql/create_tables.sql")


def create_table_if_not_exists(conn, df, table_name):
    """
    Using psycopg2.extras.execute_values() to insert the dataframe
    """
    create_table_str = "CREATE TABLE IF NOT EXISTS {} ({});".format(
        table_name, ', '.join(df.columns))

    # query = "INSERT INTO \"%s\" (%s) VALUES %%s" % (table_name, cols)
    cursor = conn.cursor()
    try:
        cursor.execute(create_table_str)
        # execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()
