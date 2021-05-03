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
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols_wrapped = [f"\"{col}\"" for col in df.columns]
    cols = ','.join(list(cols_wrapped))

    # SQL quert to execute
    create_if_not_exists = f"CREATE TABLE IF NOT EXISTS \"{table_name}\" ({cols});"
    query = "INSERT INTO \"%s\" (%s) VALUES %%s" % (table_name, cols)
    cursor = conn.cursor()
    try:
        cursor.execute(create_if_not_exists)
        execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()
