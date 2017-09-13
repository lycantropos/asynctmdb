#!/usr/bin/env bash

function export_login {
    local IFS=$'\n'
    local lines=($1)
    export TMDB_USER_NAME=${lines[0]}
    echo Running with TMDB_USER_NAME=${TMDB_USER_NAME}
    export TMDB_USER_PASSWORD=${lines[1]}
    echo Running with TMDB_USER_PASSWORD=${TMDB_USER_PASSWORD}
}

login=$(cat login)
export_login "$login"

exec "$@"
