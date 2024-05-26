.PHONY: build run migrate makemigrations

build:
    docker compose -f local.yml build

run:
    docker compose -f local.yml up

m:
    docker compose -f local.yml run web python manage.py migrate

mm:
    docker compose -f local.yml run web python manage.py makemigrations



