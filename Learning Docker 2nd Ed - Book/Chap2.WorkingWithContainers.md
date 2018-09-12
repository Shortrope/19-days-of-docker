# Chap 2: Working w Containers

## interactive container
Create and start an interactive container  

    docker run -i -t ubuntu:16.04 /bin/bash [--name ubusvr]

|option|description|
|------|-----------|
|-i | interactive mode |
|-t | pseudo Terminal assigned to the container |

Detach from an interactive container

    ^p ^q

Create continer in detached mode

    docker run -d ubuntu:16.04 /bin/bash

List running containers

    docker ps
    docker ps -a    //show all regardless of state

Attach to a running container

    docker attach id|name

Exit and stop the container

    exit

## Track changes inside a container

    docker diff id|name

## Controlling containers

    docker stop id|name       //gracefully shutdown
    docker start id|name
    docker start -a id|name   //start and attach
    docker restart id|name
    docker pause id|name
    docker unpause id|name

## Housekeeping
Remove unused containers  
`--rm` will remove the container when it exits/stops

    docker run -i -t --rm ubuntu:16.04 /bin/bash  
    docker rm id|name     //one at a time manually

Remove all containers not currently running

    docker rm $(docker ps -aq)
    docker container prune

## Building images from Containers
After making changes to a container, check the differences by running 

    docker diff id|name

Stop the running container and run:

    docker commit id|name newImageName

## Launching a container as a daemon
    docker run -d ubuntu /bin/bash -c "while true; do date; sleep 4; done"

View the output generated by the container

    docker logs id|name
