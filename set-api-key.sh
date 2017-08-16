#!/usr/bin/env bash

export API_KEY=$(cat key)
echo Running with API_KEY=${API_KEY}

exec "$@"
