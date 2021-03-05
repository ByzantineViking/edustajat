#!/usr/bin/python
from exec_pgsql_commands import exec_pgsql_commands

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        --sql
        CREATE TABLE IF NOT EXISTS municipalities (
            municipality_id INT GENERATED ALWAYS AS IDENTITY,
            municipality_name VARCHAR(255) NOT NULL,
            PRIMARY KEY(municipality_id)
        );
        """,

        """
        --sql
        CREATE TABLE IF NOT EXISTS parties (
            party_id INT GENERATED ALWAYS AS IDENTITY,
            party_name VARCHAR(255) NOT NULL,
            PRIMARY KEY(party_id)
        );
        """,


        """
        --sql
        CREATE TABLE IF NOT EXISTS municipal_representatives (
            municipal_representative_id INT GENERATED ALWAYS AS IDENTITY,
            first_name VARCHAR(5) NOT NULL,
            last_name VARCHAR(5) NOT NULL,
            municipality_id INT,

            PRIMARY KEY(municipal_representative_id),
            FOREIGN KEY (municipality_id) REFERENCES municipalities(municipality_id),
            FOREIGN KEY (party_id) REFERENCES parties(party_id)
        );
        """
    )

    exec_pgsql_commands(commands)

if __name__ == '__main__':
    create_tables()
