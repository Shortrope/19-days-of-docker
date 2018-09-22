# Deploying w Stacks

Stacks file just like docker-compose.yml file  
https://docs.docker.com/compose/compose-file/#compose-documentation

## Stack file
Same as docker compose format  
_you can reference the inspect files for the info needed in the 'stacke' file_
- version  
- services  

Example: viz.yml

    version: '3.7'

    services:
      viz:
        image: manomarks/vixualizer
        volumes:
          - "/var/run/docker.sock:/var/run/docker.sock
        ports:
          - 8090:8080
        deploy:
          placement:
            constraints:
              - node.role==manager

## docker stack
docker stack --help

    Options:
          --bundle-file string     Path to a Distributed Application Bundle file
      -c, --compose-file strings   Path to a Compose file, or "-" to read from stdin
bundle-file: is a json formated file

    docker stack deploy -c <compose-yml-file> <stack-name>
    docker stack deploy -c viz.yml viz

each stack gets its own private network by default
- network viz_default
- service viz_viz

## Commands

    docker stack ls
    docker stack services <stack-name>
    docker stack ps <stack-name>
    docker stack rm <stack-name>
    docker service scale <service-name>=n
_`docker stack services <stack-name>` same as `docker service ls`_

_`compare to `docker service create` and `docker service update`_

## Update a stack
1. Edit the stack/compose file
1. Run the - `docker stack deploy -c file.yml stack-name` - command again

## Deploy multiple services

    version: '3.7'

    services:

      customer:
        image: swarmgs/customer
        deploy:
          replicas: 4

      balance:
        image: swarmgs/balance
        ports:
          - "5000:3000"
        environment:
          MYWEB_CUSTOMER_API: "customer:3000"
        deploy:
          replicas: 2

_Notice no need to define networks_

    docker stack deploy -c cust-balance.yml cust-balance

## Similar commands
docker run  
docker service create

docker-compose  
docker stack deploy

## Trifecta SErvices for managing services
1. Compute: containers
1. Network: automaticly set up with Swarm
1. Volumes: ?? volume replicated among multi nodes


<br><br>

---

## Backup info about services

    docker service ls
    docker service inspect wp > wp.inspect
    docker service inspect mysql > mysql.inspect
    docker network inspect wpbackend > wpbackend.inspect