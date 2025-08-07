.PHONY: run build up down collectstatic restore-db help

ENV ?= dev
COMPOSE_FILE ?= $(if $(filter-out dev, ${ENV}),docker-compose.${ENV}.yml,docker-compose.yml)
ENV_FILE ?= ${ENV}.env
COMPOSE = docker compose -f "${COMPOSE_FILE}" --env-file "${ENV_FILE}"

# Запуск вместе со сборкой
run:
	${COMPOSE} up -d --build

# Сборка контейнеров
build:
	${COMPOSE} build

# Запуск контейнеров
up:
	${COMPOSE} up -d

# Остановка
down:
	${COMPOSE} down

collectstatic:
	${COMPOSE} up web -d
	docker exec web python3 manage.py collectstatic --no-input
	${COMPOSE} down web

restore-db:
	docker cp "./dbdump/db.json" web:/tmp/db.json
	@sleep 3
	docker exec web bash -c "python manage.py loaddata /tmp/db.json"

help:
	@echo "Environment:"
	@echo "  ENV: текущее окружение (${ENV})"
	@echo "  COMPOSE_FILE: файл конфигурации docker-compose (${COMPOSE_FILE})"
	@echo "  ENV_FILE: файл .env (${ENV_FILE})"
	@echo "Targets:"
	@echo "  run: Собрать и запустить"
	@echo "  build: Собрать"
	@echo "  up: Запустить"
	@echo "  down: Остановить"
	@echo "  collectstatic: Вызов collectstatic в web контейнере"
	@echo "  restore-db: Вызов loaddata dbdump/db.json в web контейнере"
