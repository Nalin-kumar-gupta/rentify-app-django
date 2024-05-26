#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

function migrate() {
    echo "Running database migrations..."
    python manage.py migrate
    if [ $? -eq 0 ]; then
        echo "Database ready"
    else
        echo "Database migration failed"
        exit 1
    fi
}

# Run migrations
migrate

function collectstatic() {
    echo "Collecting static files..."
    python manage.py collectstatic --no-input
    if [ $? -eq 0 ]; then
        echo "Collected!!"
    else
        echo "DCollect static failed!!"
        exit 1
    fi
}

collectstatic

# Start the Django development server
python manage.py runserver 0.0.0.0:8000