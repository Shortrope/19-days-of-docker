# Managing Load Balancing and Scale in Docker Swarm Mode Clusters: Mar 2018 - 2h
## Understanding Load Balancing and Service Discovery

1.1
Swarm is the clustering solution build into docker
Run containers accros multiple servers
- service discovery
- scale
- redundancy
- self healing

## Load Balancing
Make sure an incoming request goes to the right container
And that the Load is shared amongst containers

Swarm mode binds container ports to the cluster
2 options
1. Host mode publishing
    - binds a container port to a server port
    - container has exclusive use of the host port
    - very limited

1. ingress network
    - much more flexible than Host-mode publishing
    - Default in Swarm Mode
    - container port is published to the whole swarm
