# FinLit

Hackathon project for HackHarvard 2019. Developed a web application to help banks maximize impact of financial literacy workshops based on location, and display avialable workshops in a user's area.

- Best Financial Hack (Sponsored by Capital One)
- Best Connecting the Dots Overall Theme Hack (Sponsored by Harvard)
- Best Use of Google Cloud Platform 3rd Place (Sponsored by Google Cloud)

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
    (env)$ pip3 install -r requirements.txt
    (env)$ deactivate

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

Set up Django for digital ocean: return to virtualenv

    (env)$ ./manage.py createsuperuser
    (env)$ ./manage.py collectstatic
    (env)$ sudo ufw allow 8000
    (env)$ ./manage.py runserver 0.0.0.0:8000



End readme   
