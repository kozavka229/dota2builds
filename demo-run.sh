cp example.env dev.env
chmod +x ./dota2site/entrypoint.sh
make run

chmod +x ./dbdump/restore.sh
./dbdump/restore.sh "./dbdump/db.sql"
