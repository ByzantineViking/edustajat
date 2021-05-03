#!/usr/bin/python
from edustajat_service.sql.helpers.execute_sql_file import execute_scripts_from_file

def create_tables():
    """ create tables in the PostgreSQL database"""
    execute_scripts_from_file("./sql/create_tables.sql")

if __name__ == '__main__':
    create_tables()
