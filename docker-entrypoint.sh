#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"
