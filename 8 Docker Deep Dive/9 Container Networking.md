# Container Networking

## Bridge Networking
Default  
NAT  
bridge docker0  
Each bridge  
Scoped to single node  

    docker network create -d bridge myswitch
    docker network ls
    docker container run --rm -d --network myswitch alpine sleep 1d

## Overlay
Scoped to swarm  

    docker network create d overlay myovernet -o encrypted
    docker network ls
    docker container run --rm -d --replicas 3 --network myovernet alpine sleep 1d


## MACVLAN
Gives each container an IP and MAC on the local LAN ??  
Must allow promiscuous mode on host nic  

    docker network ls
    docker network inspect bridge
    docker port id|name

## Network Services
### Service Discovery
All Swarm Services are resolvable by name (on the overlay net)

    docker container run --rm -d --name pong --replicas 3 --network myovernet alpine sleep 1d
    ping pong     // from another container


### Load Balancing
Can hit any node in swarm to get to a service

    docker service create -d --name web --network overnet --replicas 2 -p 8080:80 nginx
    docker service inspect id|name --pretty



