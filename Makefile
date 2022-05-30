# dev commands

docker-dev-all: \
	docker-up-dev \
	docker-makemigrations-dev \
	docker-migrate-dev \
	docker-collectstatic-dev

docker-up-dev:
	docker compose -f docker-compose.dev.yml up -d --build

docker-down-dev:
	docker compose -f docker-compose.dev.yml down

docker-makemigrations-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations

docker-migrate-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py migrate --noinput

docker-collectstatic-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py collectstatic --no-input --clear

docker-createsuperuser-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

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


# testing commands

docker-staging-all: \
	docker-up-staging \
	docker-makemigrations-staging \
	docker-migrate-staging \
	docker-collectstatic-staging

docker-up-staging:
	docker compose -f docker-compose.staging.yml up -d --build

docker-down-staging:
	docker compose -f docker-compose.staging.yml down

docker-makemigrations-staging:
	docker compose -f docker-compose.staging.yml exec web python manage.py makemigrations

docker-migrate-staging:
	docker compose -f docker-compose.staging.yml exec web python manage.py migrate --noinput

docker-collectstatic-staging:
	docker compose -f docker-compose.staging.yml exec web python manage.py collectstatic --no-input --clear

docker-createsuperuser-staging:
	docker compose -f docker-compose.staging.yml exec web python manage.py createsuperuser

docker-shell-staging:
	docker compose -f docker-compose.staging.yml exec -it web sh

certbot-staging-1:
	sudo apt-get install certbot && \
	sudo certbot certonly --standalone --preferred-challenges http --email mattcullenmeyer@gmail.com --agree-tos -d staging.tinytrader.io 

certbot-staging-2:
	docker compose -f docker-compose.staging.yml run --rm certbot certonly --webroot --webroot-path /var/lib/letsencrypt/ --email mattcullenmeyer@gmail.com --staging --agree-tos -d staging.tinytrader.io

certbot-staging-3:
	docker compose -f docker-compose.staging.yml run --rm certbot certonly --webroot --webroot-path /var/lib/letsencrypt/ --email mattcullenmeyer@gmail.com --agree-tos -d staging.tinytrader.io 

docker-restart-staging:
	docker compose -f docker-compose.staging.yml restart
