#!/bin/bash

CONFIG_DIR=~/.config/mygithub
TOKEN_FILE=$CONFIG_DIR/github_token

read -erp 'Enter your GitHub username: ' USER_NAME
[[ -z "$USER_NAME" ]] && exit 1

read -ersp 'Enter your GitHub password: ' PASSWORD
[[ -z "$PASSWORD" ]] && exit 1 || echo -e '\n'

TMP_FILE=$(mktemp) && trap "rm -f $TMP_FILE" EXIT

HTTP_CODE=$(
  curl \
    --silent \
    --output "$TMP_FILE" \
    --write-out '%{http_code}' \
    --data '{"scopes":["repo", "read:packages"], "note":"fetch-my-repos"}' \
    --url https://api.github.com/authorizations \
    -K- <<< "--user $USER_NAME:$PASSWORD"
)

[[ $HTTP_CODE -eq 201 ]] && {
  TOKEN_URL=$(jq -r '.url' "$TMP_FILE")
  echo -e "+ Created access token at: $TOKEN_URL"
} || {
  jq -r '.' "$TMP_FILE"
  echo -e "Failed to create access token.  HTTP status code: $HTTP_CODE"
  exit 1
}

TOKEN=$(jq -r '.token' "$TMP_FILE") || {
  jq -r '.' "$TMP_FILE"
  echo -e "Failed to parse access token"
  exit 1
}

mkdir -p "$CONFIG_DIR" || {
  echo -e "Failed to create directory $CONFIG_DIR"
  exit 1
}

echo $TOKEN > "$TOKEN_FILE" ||
  echo -e "Failed to write GitHub access token to $TOKEN_FILE"
