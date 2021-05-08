

## Install packages
pip install -r requirements.txt
pip install *package*
pip freeze > requirements.txt


## Running the backend.

1. source *path*/edustajat/backend/env/bin/activate
2. python3 run.py




## Access local database

### Update and install PostgreSQL 10.4
sudo apt update
sudo apt install postgresql

### By default the postgres user has no password can only connect if ran by the postgres sytem user. The following command will assign postgres user password.
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE testdb;"

### Creating a postgres system user
sudo -u postgres createuser -s postgres

### Starting the server
sudo service postgresql start

### Checking server status
sudo service postgresql status

### Log into a database using the database postgresql user when logged into the system user postgres
sudo su postgres
psql edustajat_db postgres

### psql commands
- \? - help
- \d - list tables
- \di - list indices
- \list - list databases

### Stopping the server
sudo service postgresql stop