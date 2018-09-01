# Docker Swarm Mode

## Initialize a node

    docker swarm init --advertise-addr x.x.x.x
    docker node ls

The `run` command 

    docker run      // to start a container on a node
    docker service  // to create a task(s) on a cluster (tasks create containers)

## Service
A `service` is a definition of an app you want to run.. a desired state for an app
- image to run 
- publich ports
- mem/cpu
- metwork
- replicas

Create a Service

    docker service create --name web --replicas=2 -p 80:80 nginx
    docker service ls           // shows serives
    docker service <task> ps    // shows tasks and their state
    docker ps                   // show containers running on this node

Update a service

    docker service update --replicas=4 <task name>

## Scale

    docker service scale <task name>=4
