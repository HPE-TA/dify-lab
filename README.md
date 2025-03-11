# Dify Lab


## Dify

- 以下のサイズリミットの更新
    - UPLOAD_FILE_SIZE_LIMIT=500
    - UPLOAD_IMAGE_FILE_SIZE_LIMIT=500
    - UPLOAD_VIDEO_FILE_SIZE_LIMIT=500
    - UPLOAD_AUDIO_FILE_SIZE_LIMIT=500
    - NGINX_CLIENT_MAX_BODY_SIZE=500M
- 以下のタイムアウトの更新
    - TEXT_GENERATION_TIMEOUT_MS=600000

## Langfuse

- docker-compose.yaml の以下を書き換える
    - NEXTAUTH_URL を実IPに変更

## Firecrawl

- デフォルトの環境変数ファイル(`apps/api/.env.example`)をルートディレクトリにコピーして以下を編集
    - USE_DB_AUTHENTICATION を false に変更
    - TEST_API_KEY を fc-Hello-GenA1 に変更

## TLS証明書

### CA 秘密鍵
```
openssl genrsa -out ca-key.pem 2048
```

### CA 証明書署名要求(CSR)
```
openssl req -new -key ca-key.pem \
  -subj "/C=JP/ST=Tokyo/O=HPE/CN=TA Root CA" \
  -out ta-ca.csr
```

### CA 証明書(自己署名)
```
openssl x509 -req -in ta-ca.csr \
  -signkey ca-key.pem -out ta-ca.crt -days 3650
```

### 秘密鍵
```
openssl genrsa -out server.key 2048
```

### 証明書署名要求(CSR)
```
openssl req -new -key server.key \
  -subj "/C=JP/ST=Tokyo/O=HPE/CN=*.example.com" \
  -out server.csr
```

### 署名
```
openssl x509 -req -days 3650 \
  -extfile <(printf "subjectAltName=DNS:example.com,DNS:www.example.com") \
  -in server.csr \
  -CA ta-ca.crt -CAkey ca-key.pem -CAcreateserial \
  -out server.crt
```
