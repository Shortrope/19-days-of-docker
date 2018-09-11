# Chap 1

## 1. Install

sudo curl -sSL https://get.docker.io/ | sh
sudo wget -qO- https://get.docker.io/ | sh

docker version
  client, client API
  server, server API
docker info 
  
### client server communication
  /var/run/docker.sock
  port 2375   //not enabled by default


### First docker image
Get a docker image
docker pull hello-world

List you docker images
docker images

Run the D image
docker run hello-world

### T-Shooting
service docker status

-------------
## 2. Get images

### Docker registry
- Docker Hub (index.docker.io)
- Quay
- Google container registry
- AWS container registry

docker pull name
docker pull name:1.23   //get specific version
docker pull -a name     // get all available versions
docker pull id|name
docker pull repo.url/name

docker search name
