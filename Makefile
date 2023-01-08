build-dev:
	docker-compose build

up-dev:
	docker-compose up -d

format:
	black . && isort