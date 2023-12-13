# Define variables
COMPOSE_FILE := docker-compose.yml
CMD := docker compose -f $(COMPOSE_FILE)

# Main targets
.PHONY: help up down stop clean prune all logs

all: up

# Show logs for all containers
logs:
	$(CMD) logs -f

up: ## Start containers defined in docker-compose.yml
	$(CMD) up -d --build

down: ## Stop and remove containers defined in docker-compose.yml
	$(CMD) down

stop: ## Stop containers defined in docker-compose.yml
	$(CMD) stop

clean: stop ## Stop and remove containers, networks, and volumes
	$(CMD) down -v --remove-orphans
	$(CMD) rm -f

prune: clean ## Remove all unused containers, networks, images, and volumes
	docker system prune -af