cp example.env dev.env
chmod +x ./dota2site/entrypoint.sh
make run
make restore-db
