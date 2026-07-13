.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / \
		{printf "\033[38;2;98;209;150m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

export
NOW = $(shell date '+%Y%m%d-%H%M%S')

#######################################################################################################################
# vllm-gemma4
#######################################################################################################################
IMAGE_NAME = vllm/vllm-openai
IMAGE_TAG = v0.24.0

up-vllm-gemma4: ## Start vllm-gemma4.
	docker run -d --name vllm-gemma4 -p 8001:8000 \
		--shm-size=16g \
		--gpus '"device=0"' \
		-v /home/share/models/llm:/llm \
		-v $(XDG_CACHE_HOME):/root/.cache \
		-v $(shell pwd)/templates:/templates:ro \
		$(IMAGE_NAME):$(IMAGE_TAG) \
		--model /llm/gemma-4-31B-it \
		--served-model-name google/gemma-4-31B-it \
		--quantization fp8 \
		--kv-cache-dtype fp8 \
		--max-model-len 64K \
		--speculative-config.model /llm/gemma-4-31B-it-assistant \
		--speculative-config.num_speculative_tokens 3 \
		--enable-auto-tool-choice \
		--tool-call-parser gemma4 \
		--chat-template /templates/tool_chat_template_gemma4.jinja \
		--reasoning-parser gemma4 \
		--gpu-memory-utilization 0.8 \
		--host 0.0.0.0 --port 8000

down-vllm-gemma4: ## Stop vllm-gemma4.
	docker stop vllm-gemma4 || :
	docker rm vllm-gemma4 || :

ps-vllm-gemma4: ## Status vllm-gemma4.
	docker ps -a -f name=vllm-gemma4 || :

log-vllm-gemma4: ## Log vllm-gemma4.
	docker logs -f vllm-gemma4 || :
