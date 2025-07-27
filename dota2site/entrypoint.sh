#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate

if [ "$ENV" = "dev" ] && [ "$USE_CDN" = "1" ]; then
  echo "Collect static..."
  python3 manage.py collectstatic --no-input
fi

if [ "$ENV" = "prod" ] || [ "$USE_CDN" = "1" ]; then
  echo "Recopy static..."
  rm -rf /staticfiles/*
  cp -rf ./staticfiles/* /staticfiles/
fi

exec "$@"