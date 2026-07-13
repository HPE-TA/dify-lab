.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / \
		{printf "\033[38;2;98;209;150m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

export
NOW = $(shell date '+%Y%m%d-%H%M%S')

#######################################################################################################################
# embedding
#######################################################################################################################
IMAGE_NAME = vllm/vllm-openai
IMAGE_TAG = v0.24.0

up-embedding: ## Start embedding.
	docker run -d --name embedding -p 8002:8000 \
		--shm-size=16g \
		--gpus '"device=0"' \
		-e HF_TOKEN \
		-v $(XDG_CACHE_HOME):/root/.cache \
		$(IMAGE_NAME):$(IMAGE_TAG) \
		--model cl-nagoya/ruri-v3-310m \
		--gpu-memory-utilization 0.05 \
		--host 0.0.0.0 --port 8000

down-embedding: ## Stop embedding.
	docker stop embedding || :
	docker rm embedding || :

ps-embedding: ## Status embedding.
	docker ps -a -f name=embedding || :

log-embedding: ## Log embedding.
	docker logs -f embedding || :


test-vllm-embedding-models: ## test-vllm-embedding-models
	curl --request GET \
		--header "Content-Type: application/json" \
		--header "Authorization: Bearer no-key" \
		--url http://localhost:8002/v1/models | jq .

test-vllm-embedding-1: ## test-vllm-embedding-1
	curl --request POST \
		--header "Content-Type: application/json" \
		--header "Authorization: Bearer no-key" \
		--url http://localhost:8002/v1/embeddings \
		--data '{"model": "cl-nagoya/ruri-v3-310m", "input": "スイカ割りは目隠しをして行います。"}'

test-vllm-embedding-long: ## test-vllm-embedding-long
	curl --request POST \
		--header "Content-Type: application/json" \
		--header "Authorization: Bearer no-key" \
		--url http://localhost:8002/v1/embeddings \
		--data '{"model": "cl-nagoya/ruri-v3-310m", "input": "機械学習をはじめとする AI 技術は進化しながら普及の一途を辿り、様々な産業の競争力の源泉と なるだけでなく、既存の産業構造を破壊・変革し、新たな産業を創出するようになってきている。そ れに伴い、AI 技術を用いた製品やサービス（AI プロダクト）が生活や社会、経済に及ぼす影響も大 きくなってきている。 その一方で、AI 技術は進化途上であるとともに、ハードウェアや従来型のソフトウェア、サービ スなどに比べ、その技術的特質により、品質の把握、評価、説明、管理など品質保証が非常に難しい。 特に機械学習ではデータの学習によりふるまいが帰納的に決定されるため、従来型のソフトウェア に対する品質保証手段が利用できない。開発プロセスの管理による品質保証が寄与する割合も小さ い。したがって AI プロダクトの品質保証技術が確立されたとは到底言いがたい状況にある。すなわ ち我々の生活や社会、経済には、AI プロダクトの品質事故という甚大なリスクが内在されているの である。 同時に注意すべきなのは、AI 技術が持つ技術的特質を無視し AI プロダクトの品質に社会が過度 の期待を持つことが、品質保証のための過度な活動を要請し、AI 技術の適切な活用や適時のリリー ス、さらなる進化を妨げる圧力を与えてしまう点である。我々は AI プロダクトの品質リスクを軽減 するとともに、過度の品質圧力を予防し、AI 技術が安心して活用され進化できるようにする必要が ある。 したがって、我々が安心・安全な生活や社会、経済を営んでいくためには、AI プロダクトに対す る品質保証技術の調査・体系化、適用支援・応用、研究開発が急務である。同時に、AI プロダクト の品質に対して、技術的特質を踏まえた適切な理解を社会が持ちうるような啓発活動も進めていか ねばならない。 そこで我々は、AI プロダクトの品質保証のためのガイドラインを発行する。このガイドラインは、 各組織において AI 技術への過度の期待を予防し、適切な活用や適時のリリースを行うための、AI プロダクトの品質保証に対する共通的な指針を与えるものである。 機械学習に代表される AI 技術は著しく速く進化しているため、本ガイドラインは年次程度に定期 的に更新される。各組織や産業において標準的な文書を作成したり適合性の程度を評価したりする 場合には、その点について十分に考慮する必要がある。"}'