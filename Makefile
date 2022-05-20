# local commands

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down

docker-makemigrations:
	docker compose exec web python manage.py makemigrations

docker-migrate:
	docker compose exec web python manage.py migrate --noinput

docker-collectstatic:
	docker compose exec web python manage.py collectstatic --no-input --clear

docker-createsuperuser:
	docker compose exec web python manage.py createsuperuser

# production commands

docker-up-prod:
	docker compose -f docker-compose.prod.yml up -d --build

docker-down-prod:
	docker compose -f docker-compose.prod.yml down

docker-makemigrations-prod:
	docker compose -f docker-compose.prod.yml exec web python manage.py makemigrations

docker-migrate-prod:
	docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

docker-collectstatic-prod:
	docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

docker-createsuperuser-prod:
	docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
