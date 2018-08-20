# Chap 5

## 5. Private Docker infrastructure

### Docker Registry
Tcp port 5000  
Storage degault path: /var/lib/registry

    docker run -d -p 5000:5000 --restart=always --name registry registry:2

Test the Registry

    docker pull hello-world
    docker tag hello-world localhost:5000/hello-world
    docker images
    docker push localhost:5000/hello-world
    docker rmi localhost:5000/hello-world
    docker pull localhost:5000/hello-world

    docker stop registry 
    docker rm -v registry

Create with Storage

    docker run -d -p 5000:5000 --restart=always --name registry -v `pwd`/data:/var/lib/registry registry:2

With SSL certificates: p.105
Starting w Docker Compose p.108

### Webhook notifications 
p.110

### Registry HTTP API 
p.111  
https://github.com/docker/distribution/blob/master/docs/spec/api.md.

