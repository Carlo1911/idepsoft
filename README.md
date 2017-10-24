# Idepsoftware =D

## THIS README ASSUMES THE FOLLOWING:
- **git** is installed and this repository has been downloaded, it's location is noted on the following item. 
  Repository download is usually handled by git, but it could have been copied with zip, as long as no location 
  changes were made.
- Directory used is /opt/apps/idepsoft. This is the repository directory.
- Proper language and timezone are configured on the server.

## Install:

```sh

sudo apt-get update
sudo apt-get install -y python3-pip libjpeg-dev libfreetype6  libfreetype6-dev zlib1g-dev libpq-dev libffi-dev git build-essential libssl-dev libffi-dev python3-dev
sudo apt-get install -y redis-server
sudo apt-get install -y postgresql postgresql-contrib postgresql-client
sudo apt-get install -y nginx
```

- Create virtualenv directory: `mkdir env`
- Create environment: `virtualenv --no-site-package --distribute env`
- Load virtualenv: `source env/bin/activate`
- Install dependencies: `pip3 install -r requirements/local.txt` (for development)
- Install dependencies: `pip3 install -r requirements/production.txt` (for production)
- Create database user and set a password and create a db for the application

```sh
sudo su - postgres
createuser --interactive idepsoft_user; (No dar permisos)
psql
 ALTER USER idepsoft_user WITH PASSWORD 'idepsoft_password';
 CREATE DATABASE idepsoftdb WITH OWNER idepsoft_user;
 \q
exit
```

- Create .env file: `touch .env`
- Edit settings params in .env file with the below values (customize according to your needs, default sample works on most occasions):

```sh
SECRET_KEY="THIS_MUST_NOT_BE_EMPTY"
DOMAIN="http://wawared.minsa.gob.pe"
DB_NAME="idepsoftdb"
DB_USER="idepsoft_user"
DB_PASSWORD="idepsoft_password"
DB_HOST="localhost"
DB_PORT="5432"

EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="*****@gmail.com"
EMAIL_HOST_PASSWORD="*****"
EMAIL_HOST_PORT="587"

BROKER_URL="redis://localhost:6379/"
BROKER_RESULT_BACKEND="redis://localhost:6379/"
STATIC_URL="/static/"
MEDIA_URL="/media/"
```

- Make migrations/(estructura to database): python manage.py migrate

- Load data:

```sh
python manage.py loaddata apps/ubigeo/fixtures/*.json
python manage.py loaddata apps/pacientes/fixtures/*.json
python manage.py loaddata apps/controles/fixtures/*.json
```

- Collect static (add static django): `python manage.py collectstatic --noinput`  
- Run Django: python manage.py runserver

# Configure nginx

For nginx:

- Create a configuration file on /etc/nginx/sites-available/ named `vih.com.conf` and copy the sample configuration file nginx.vih.conf.samlple content's into it (modify if required).

```sh
sudo cp samples/idepsoft.nginx.conf.sample /etc/nginx/sites-available/idepsoft.com.conf
```

- Create simbolyc link for the new configuration file and reload nginx:
- Optional, validate nginx configuration, delete nginx default configuration file symbolic link.

```sh
sudo ln -s /etc/nginx/sites-available/idepsoft.com.conf /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo nginx -s reload
```
