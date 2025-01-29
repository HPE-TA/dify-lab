.DEFAULT_GOAL := help

export
NOW = $(shell date '+%Y%m%d-%H%M%S')


IMAGE_NAME = xprobe/xinference
IMAGE_TAG = v1.2.1

up-xinference: ## Start xinference.
	docker run -d --name xinference -p 9997:9997 \
		--shm-size=16g \
		--gpus all \
		-v $(XDG_CACHE_HOME):/root/.cache \
		-v $(XDG_CACHE_HOME)/.xinference:/root/.xinference \
		-e HUGGING_FACE_HUB_TOKEN \
		$(IMAGE_NAME):$(IMAGE_TAG) \
		xinference-local -H 0.0.0.0

down-xinference: ## Stop xinference.
	docker stop xinference || :
	docker rm xinference || :

log-xinference: ## Log xinference.
	docker logs -f xinference || :



.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / \
		{printf "\033[38;2;98;209;150m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
