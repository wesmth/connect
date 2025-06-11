#!/usr/bin/env bash
# script pra buildar no Render

echo "Rodando migrations..."
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput
