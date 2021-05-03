from edustajat_service.db.exec_pgsql_commands import exec_pgsql_commands

def execute_scripts_from_file(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()
    # all SQL commands (split on ';')
    sql_commands = sql_file.split(';')

    sql_commands = list(filter(lambda x: not str.isspace(x), sql_commands))

    exec_pgsql_commands(sql_commands)
