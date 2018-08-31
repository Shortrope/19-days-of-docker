# How to instantiate these images

docker build -t myapache2 .
docker run -rm -d -p 8080:80 myapache2

docker build -t myhttpd .
docker run -rm -d -p 8081:80 myhttpd
