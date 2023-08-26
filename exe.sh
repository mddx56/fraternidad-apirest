#!/bin/bash

sudo apt update
sudo apt install -y git

git clone https://github.com/waltherx/fraternidad-apirest.git

sudo apt install -y python3-pip

cd fraternidad-apirest

pip3 install -r requirements.txt

echo "DB_NAME=farter
DB_USER=fl0user
DB_PASSWORD=8IXE2jLHxgnq
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=django-insecure-f4ai73k+ku5w=-mz!+%*4l$w%&tmq(j)3tq@yi^=q1z-n)$c&_
DEBUG=False
EMAIL_USER=172e76d9ae4fc0
EMAIL_PASSWORD=e5b8da69ac0589" > .env

sudo apt install -y postgresql postgresql-contrib

sudo service postgresql start

sudo -u postgres psql -c "CREATE DATABASE farter;"
sudo -u postgres psql -c "CREATE USER fl0user WITH PASSWORD '8IXE2jLHxgnq';"
sudo -u postgres psql -c "ALTER ROLE fl0user SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE fl0user SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE fl0user SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE farter TO fl0user;"

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input

#ojo con esta linea te pide username y password
python3 manage.py createsuperuser

uvicorn fraternidad.asgi:application --reload