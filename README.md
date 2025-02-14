# Dify Lab


## Dify

- 以下のサイズリミットの更新
    - UPLOAD_FILE_SIZE_LIMIT
    - UPLOAD_IMAGE_FILE_SIZE_LIMIT
    - UPLOAD_VIDEO_FILE_SIZE_LIMIT
    - UPLOAD_AUDIO_FILE_SIZE_LIMIT
    - NGINX_CLIENT_MAX_BODY_SIZE

## Langfuse

- docker-compose.yaml の以下を書き換える
    - NEXTAUTH_URL を実IPに変更
    - container_name を削除
