# Adding Nodes

Swarm Mode automatically creates and distributes certificates for security

Initialize Swarm Mode  

    docker swarm init --advertise-addr x.x.x.x

Join an existing Swarm run the command displayed by docker  

    root@dm1:~# d swarm join-token manager
    To add a manager to this swarm, run the following command:

        docker swarm join --token SWMTKN-1-5nt6eai59cmrwsy1yd5nk5gxp34rd1t8vtnzvvil8cceqhjl1y-dsidszuon3h3mzx8lwhdnzq6s 192.168.1.21:2377

    root@dm1:~# d swarm join-token worker
    To add a worker to this swarm, run the following command:

        docker swarm join --token SWMTKN-1-5nt6eai59cmrwsy1yd5nk5gxp34rd1t8vtnzvvil8cceqhjl1y-06zabhody4qevf4dh92t469r2 192.168.1.21:2377

Remove a node from a Swarm  

    docker swarm leave          // on the node
    docker node rm NODE_NAME    // from a manager

Inspect a node  

    docker node inspect NODE_NAME
    docker node ps
    docker node ps NODE_NAME

Services w published ports are connected to the `ingress` network  

    root@dm1:~# d network ls
      NETWORK ID          NAME                DRIVER              SCOPE
      7b12b4af9aa9        bridge              bridge              local
      df0bdff49efd        docker_gwbridge     bridge              local
      59b03541f539        host                host                local
      uplld7rfqa6t        ingress             overlay             swarm
      cda9117332ac        none                null                local

Change node role - manager/worker  

    docker node promote NODE_NAME     // promote a worker node to a manager
    docker node demote NODE_NAME      // demote a manager node to a worker

Change node options with `update`  

    docker node update --help

Move all containers to other nodes so you can run some maintenance  

    docke node update --availability drain

Mode of service create `replicate|global`
`replcate` is the default, can scale any number of containers  
`global` will put one container on each node.  Good for monitoring containers


---
### Visualizer

    root@dm1:~# docker service create --name viz -p 8090:8080 \
     --constraint=node.role==manager \
     --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
     dockersamples/visualizer