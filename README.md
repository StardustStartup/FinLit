# HackED

Hackathon project for HackED at Boston University. Developing a preventative care web application to maximize

## Build Setup for Front End

    bash
### Install dependencies.
    npm install

### Serve with hot reload.
    npm run serve

## Set Up Backend

Install dependencies:

    $ sudo apt update
    $ sudo apt install nginx curl git
    $ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib 
    $ sudo apt install python3-virtualenv python3-psycopg2 binutils libproj-dev gdal-bin postgis

Initialize repository:

    $ git clone https://github.com/StardustStartup/HackED.git
    $ cd backend
    $ virtualenv -p python3 env
    $ source env/bin/activate
    (venv)$ pip3 install -r requirements.txt
    (venv)$ deactivate

Set up PostgreSQL/PostGIS:

    $ sudo -u postgres createuser medout --interactive
    $ sudo -u postgres createdb medout_db
    $ sudo -u postgres psql
    postgres=# alter user medout with encrypted password 'medout';
    postgres=# grant all privileges on database medout_db to medout;
    postgres=# \c medout_db;
    medout_db=# CREATE EXTENSION postgis;
    medout_db=# \q
    $ sudo systemctl enable postgresql
    $ sudo systemctl start postgresql

**Be sure to modify /backend/settings.py to reflect database credentials, host, and port.**

Make sure localhost IP address (not 127.0.0.1) is added to ALLOWED_HOSTS in settings.py for deployment.

Set up Django for digital ocean!


End readme   