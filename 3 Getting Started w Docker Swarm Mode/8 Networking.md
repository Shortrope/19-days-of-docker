# Networking
The `ingress` network is for routing to services  which are publishing ports.  
And to facilitate internal load balancing between the services  

- no service discomver in the ingress network

## Create a Network
For containter to container communication

    docker network create \
      --driver overlay \
      --subnet=10.0.9.0/24 \
      backend

If you do not specify a subnet, it will be created for you.  
The subnet will not be assigned until the first time you use it.  If you run inspect the `Subnet` will
not be defined

## Connect service to the network

    docker service create --name web \
      -p 8080:80 \
      --network backend
      wordpress

Fro the mysql

    docker service create --name db \
      --network backend
      mysql

Tell Wordpress service the name of the service for the db

    docker service update --env-add MYSQL_HOST=db:3306 web

Get the dns records for the services on overlay network

    docker exec -it <id> bash
    dig db
    dig tasks.db

EndpointSpec.Mode =   
- vip   //virtual ip  
- dnsrr // dns round robin

## Ports for `overlay` network
To use the overlay network across _nodes_ requires ports 
- tcp/udp 7946  for container network descovery
- udp 4789  for container overlay network