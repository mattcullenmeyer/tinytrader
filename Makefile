# dev commands

docker-all: \
	docker-up \
	docker-makemigrations \
	docker-migrate \
	docker-collectstatic

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

docker-prod-all: \
	docker-up-prod \
	docker-makemigrations-prod \
	docker-migrate-prod \
	docker-collectstatic-prod

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

docker-certbot-staging:
	docker compose -f docker-compose.prod.yml run --rm certbot certonly --webroot --webroot-path /var/www/certbot --email mattcullenmeyer@gmail.com --staging --agree-tos -d staging.tinytrader.io

docker-certbot:
	docker compose -f docker-compose.prod.yml run --rm certbot certonly --webroot --webroot-path /var/www/certbot --email mattcullenmeyer@gmail.com --agree-tos -d staging.tinytrader.io 

# testing commands

docker-testing-all: \
	docker-up-testing \
	docker-makemigrations-testing \
	docker-migrate-testing \
	docker-collectstatic-testing

docker-up-testing:
	docker compose -f docker-compose.testing.yml up -d --build

docker-down-testing:
	docker compose -f docker-compose.testing.yml down

docker-makemigrations-testing:
	docker compose -f docker-compose.testing.yml exec web python manage.py makemigrations

docker-migrate-testing:
	docker compose -f docker-compose.testing.yml exec web python manage.py migrate --noinput

docker-collectstatic-testing:
	docker compose -f docker-compose.testing.yml exec web python manage.py collectstatic --no-input --clear

docker-createsuperuser-testing:
	docker compose -f docker-compose.testing.yml exec web python manage.py createsuperuser

docker-shell-testing:
	docker compose -f docker-compose.testing.yml exec -it web sh
