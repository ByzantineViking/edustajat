from edustajat_service.db.exec_pgsql_commands import exec_pgsql_commands


def execute_sql_file(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()
    # all SQL commands (split on ';')
    sql_commands = sql_file.split(';')

    sql_commands = [x for x in sql_commands if x.strip()]
    exec_pgsql_commands(sql_commands)
