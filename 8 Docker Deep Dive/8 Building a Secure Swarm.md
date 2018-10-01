# Building a Secure Swarm

## Secure Cluster

## Orchestrator

- Manager Nodes
- Worker Nodes

## Swarm Mode
- Single-engine Mode
- Swarm Mode  

SwarmKit

Create a Manager

    docker swarm init

Each swarm has a single `Leader` Manager.. others are `Follower` Managers  
Manager HA best Practice: Have 3, 5 or 7.. not more
Connect Manageres on `Fast, Reliable` network

Built a
- CA store
- Cluster Store
- Cryptographic tokens for Managers and Workers

Each `Node` gets a certificate
- Name
- ID
- Swarm it belongs to 
- Role: Manager | Worker
- Expiration

Check if Node is in swarm mode

    docker info
    docker node ls
    docker swarm join-token manager
    docker swarm join-token worker
    docker swarm join-token --rotate worker

Autolock a Swarm (for managers)

    docker swarm init --autolock
    docker swarm update --autolock=true

To rejoin:

    docker swarm unlock
    Please enter unlock key: