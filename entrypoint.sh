#!/bin/sh
set -e

echo "Rodando migrations..."
poetry run flask db upgrade

echo "Iniciando aplicação..."
exec "$@"
