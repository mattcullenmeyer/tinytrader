# dev commands

docker-all-dev: \
	docker-up-dev \
	docker-makemigrations-dev \
	docker-migrate-dev

docker-up-dev:
	docker compose -f docker-compose.dev.yml up -d --build

docker-down-dev:
	docker compose -f docker-compose.dev.yml down

docker-logs-dev:
	docker compose -f docker-compose.dev.yml logs

docker-makemigrations-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations

docker-migrate-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py migrate --noinput

docker-createsuperuser-dev:
	docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

# staging commands

docker-all-staging: \
	docker-up-staging \
	docker-makemigrations-staging \
	docker-migrate-staging \
	docker-collectstatic-staging

docker-up-staging:
	docker compose -f docker-compose.staging.yml up -d --build

docker-down-staging:
	docker compose -f docker-compose.staging.yml down

docker-logs-staging:
	docker compose -f docker-compose.staging.yml logs

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
