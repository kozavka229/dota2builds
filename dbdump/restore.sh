#!/usr/bin/env bash

docker cp "$1" db:/tmp/db.sql
sleep 3
docker exec db bash -c "psql -U postgres -d dota2site < /tmp/db.sql"
