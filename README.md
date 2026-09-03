# Dify Lab
<a id="markdown-dify-lab" name="dify-lab"></a>

<!-- TOC -->

- [Dify Lab](#dify-lab)
  - [Dify](#dify)
  - [vLLM](#vllm)
    - [Prometheus/Grafana](#prometheusgrafana)
  - [Langfuse](#langfuse)
  - [Firecrawl](#firecrawl)

<!-- /TOC -->


## Dify
<a id="markdown-dify" name="dify"></a>

`.env` ファイルでの設定変更

- ファイルアップロードサイズリミットの更新
  - UPLOAD_FILE_SIZE_LIMIT=500
  - UPLOAD_IMAGE_FILE_SIZE_LIMIT=500
  - UPLOAD_VIDEO_FILE_SIZE_LIMIT=500
  - UPLOAD_AUDIO_FILE_SIZE_LIMIT=500
  - NGINX_CLIENT_MAX_BODY_SIZE=500M
- ファイルアップロード数リミットの更新
  - UPLOAD_FILE_BATCH_LIMIT=50
  - BATCH_UPLOAD_LIMIT=50
- タイムアウトの更新
    - TEXT_GENERATION_TIMEOUT_MS=600000
    - WORKFLOW_GENERATION_TIMEOUT_MS=1800000
- ナレッジのchunkサイズの拡張
  - INDEXING_MAX_SEGMENTATION_TOKENS_LENGTH=8000
- ナレッジのTop kの拡張
  - TOP_K_MAX_VALUE=20
- 処理可能なオブジェクト配列、テキスト配列の最大長の拡張
  - CODE_MAX_OBJECT_ARRAY_LENGTH=100
  - CODE_MAX_STRING_ARRAY_LENGTH=100
- アカウント作成時のトークンの有効期限延長
  - INVITE_EXPIRY_HOURS=240
- プラグインで画像を扱うための設定
  - FILES_URL=http://...
- Unstructured APIを有効化
  - COMPOSE_PROFILES=`${VECTOR_STORE:-weaviate},${DB_TYPE:-postgresql},collaboration,unstructured`
  - ETL_TYPE=Unstructured
  - UNSTRUCTURED_API_URL=http://unstructured:8000/general/v0/general
- アップロードできるファイルタイプを制限
  - UPLOAD_FILE_EXTENSION_BLACKLIST=exe,bat,cmd,com,scr,vbs,ps1,msi,dll
- Weaviateのtokenizerを日本語仕様に変更
  - WEAVIATE_TOKENIZATION=gse
  - WEAVIATE_ENABLE_TOKENIZER_GSE=true
- ハウスキープ有効化
  - WORKFLOW_LOG_CLEANUP_ENABLED=true
  - ENABLE_CLEAN_EMBEDDING_CACHE_TASK=true
  - ENABLE_CLEAN_UNUSED_DATASETS_TASK=true
  - ENABLE_CLEAN_MESSAGES=true
- ハウスキープ期間
  - SANDBOX_EXPIRED_RECORDS_RETENTION_DAYS=60
  - WORKFLOW_LOG_RETENTION_DAYS=60
  - PLAN_SANDBOX_CLEAN_DAY_SETTING=60
- コラボレーションモードの無効化
  - ENABLE_COLLABORATION_MODE=false
- sandboxがprivate networkにアクセスすることを許可する
  - SSRF_PROXY_ALLOW_PRIVATE_IPS=...
- Agentが通信するためのAPI tokenをデフォルトから更新する(以下の２つで同じ値を指定する必要がある)
  - DIFY_AGENT_API_TOKEN
  - AGENT_BACKEND_API_TOKEN

**Air-Gapped 環境用**

- MARKETPLACE_ENABLED=false
- CHECK_UPDATE_URL=
- HOSTED_FETCH_APP_TEMPLATES_MODE=builtin
- HOSTED_FETCH_APP_TEMPLATES_REMOTE_DOMAIN=
- HOSTED_FETCH_PIPELINE_TEMPLATES_MODE=builtin
- HOSTED_FETCH_PIPELINE_TEMPLATES_REMOTE_DOMAIN
- プラグインインストール時のpythonライブラリダウンロードURL
  - PIP_MIRROR_URL=http://...:8080/simple/
  - PIP_TRUSTED_HOST=...
  - PLUGIN_IGNORE_UV_LOCK=true

**Difyのインスタンスをポートずらしで起動するとき**

- EXPOSE_NGINX_PORT=1080
- EXPOSE_NGINX_SSL_PORT=1443
- APP_WEB_URL=http://...:1080
- FILES_URL=http://...:1080
- EXPOSE_PLUGIN_DEBUGGING_PORT=5004


## vLLM
<a id="markdown-vllm" name="vllm"></a>

https://recipes.vllm.ai/


### Prometheus/Grafana
<a id="markdown-prometheus%2Fgrafana" name="prometheus%2Fgrafana"></a>

https://docs.vllm.ai/en/stable/examples/observability/prometheus_grafana/



## Langfuse
<a id="markdown-langfuse" name="langfuse"></a>

- docker-compose.yaml の以下を書き換える
  - NEXTAUTH_URL を実IPに変更

## Firecrawl
<a id="markdown-firecrawl" name="firecrawl"></a>

- デフォルトの環境変数ファイル(`apps/api/.env.example`)をルートディレクトリにコピーして以下を編集
  - USE_DB_AUTHENTICATION を false に変更
  - TEST_API_KEY を fc-Hello-GenA1 に変更
