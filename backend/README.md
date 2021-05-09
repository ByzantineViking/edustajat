
## Setup python package

### Install packages
pip install -r requirements.txt
pip install *package*
pip freeze > requirements.txt

### Development .env
export APP_SETTINGS="edustajat_service.db.config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/edustajat_db"
FLASK_APP=api.py
FLASK_ENV=development

### Development database.ini
\[postgresql\]
host=localhost
database=db_name
user=postgres
password=password


## Running the backend.

1. source *path*/edustajat/backend/env/bin/activate
2. python3 run.py




## Access local database

### Update and install PostgreSQL 10.4
sudo apt update
sudo apt install postgresql

### By default the postgres user has no password can only connect if ran by the postgres sytem user. The following command will assign postgres user password.
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE edustajat_db;"

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
- \dS *table_name* - columns in a table
- 
    1. \x - Toggle display mode
    2. TABLE *table_name*; - Show data points in a table

### Stopping the server
sudo service postgresql stop


## Access heroku database
- see db used: heroku addons
- detailed posgres info: (watch) heroku pg:info
- app logs: heroku logs -t
- db logs: heroku logs -p postgres -t

## Establish db connection
heroku pg:psql

## Keeping local database up to date with heroku
As system user postgres:
1. Drop the local database
psql
DROP DATABASE IF EXISTS edustajat_db;
2. Pull heroku database
heroku pg:pull DATABASE_URL edustajat_db