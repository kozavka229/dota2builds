.PHONY: run build up down collectstatic help

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
	docker exec web python3 manage.py collectstatic --no-input

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
