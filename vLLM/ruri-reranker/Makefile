.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / \
		{printf "\033[38;2;98;209;150m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

export
NOW = $(shell date '+%Y%m%d-%H%M%S')

#######################################################################################################################
# reranker
#######################################################################################################################
IMAGE_NAME = vllm/vllm-openai
IMAGE_TAG = v0.24.0

up-reranker: ## Start reranker.
	docker run -d --name reranker -p 8003:8000 \
		--shm-size=16g \
		--gpus '"device=0"' \
		-e HF_TOKEN \
		-v $(XDG_CACHE_HOME):/root/.cache \
		$(IMAGE_NAME):$(IMAGE_TAG) \
		--model cl-nagoya/ruri-v3-reranker-310m \
		--gpu-memory-utilization 0.05 \
		--host 0.0.0.0 --port 8000

down-reranker: ## Stop reranker.
	docker stop reranker || :
	docker rm reranker || :

ps-reranker: ## Status reranker.
	docker ps -a -f name=reranker || :

log-reranker: ## Log reranker.
	docker logs -f reranker || :


test-vllm-reranker-models: ## test-vllm-reranker-models
	curl --request GET \
		--header "Content-Type: application/json" \
		--header "Authorization: Bearer no-key" \
		--url http://localhost:8003/v1/models | jq .