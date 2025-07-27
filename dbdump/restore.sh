#!/usr/bin/env bash

docker cp "${1}" db:/tmp/db.sql
sleep 5
docker exec db bash -c "psql -U ${2} -d ${3} < /tmp/db.sql"