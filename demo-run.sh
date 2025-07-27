chmod +x init.sh
./init.sh

cp example.env dev.env
./dev.sh build
./dev.sh up -d

./dbdump/restore.sh ./dbdump/db.sql postgres dota2site
