# Reconciling a Desired State

## Contraints
--constraint node.hostname==dw3


## Remove a node
The node must be down and then leave the swarm

    docker node rm dw4

## Remove a service

    docker service rm web1

## Pause a service so it does not execute again
Scale it to 0

    docker service scale web1=0