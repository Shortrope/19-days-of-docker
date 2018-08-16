# MySQL Docker Container

docker run --name mak_mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=wordpress -p 3306:3306 -d mysql

docker ps
docker logs mak_mysql

This will connect to the 'bridge' 172.17.0.x/16 network