#!/usr/bin/env bash

export TMDB_API_KEY=$(cat key)
echo Running with TMDB_API_KEY=${TMDB_API_KEY}

exec "$@"
