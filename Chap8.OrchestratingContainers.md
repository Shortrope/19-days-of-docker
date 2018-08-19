# Orchestrating Containers

## Inbuilt Service Discovery
- Docker implements an embedded DNS for service discovery. So containers can discover each other.  
- The embedded DNS uses IP address 127.0.0.11

Example:

    docker network create mybridge
    docker network inspect mybridge
    docker run -itd --net mybridge --name testdns ubuntu
    docker container inspect --format '{{.NetworkSettings.Networks.mybridge.IPAddress}} testdns
    docker container exec testdns cat /etc/resolv.conf
    docker container run --rm --net mybridge busybox ping -c 2 testdns

## Linking Containers
The new method of embedded DNS is highly preferred over the traditional container-linking techniques  
Container Linking is cumbersome, time consuming and error prone!

Source - Recipient : The recipient gets info about the source but not vise versa.

Use the `--link` options in `docker run` to link a source container to a recipient container

    --link <container> <alias>

- `<container>` is the 'source' container
- `<alias>` is the name seen by the receipiant container

Serveral environment variables are sent to the receipiant: NAME, ENV, PORT

_I only did a quick read thru of this section as it is not recommended to use this method!_

## Orchestration of Containers
