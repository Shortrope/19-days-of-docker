# Chap 6: Running Services in a Container

## Container Networking
    docker network ls  
    docker network inspect  
    docker network create  
    docker network rm  
    docker network connect  
    docker network disconnect  

Three Networks exist by default
- bridge
- host
- none

The 'bridge' network is an internal NAT'ed network - 172.17.0.x
The 'host' network shares the host IP address and ports  
The 'none' network only has the loopback interface - lo

Other networks available

- overlay
- macvlan
- ipvlan

A container attaches to 'bridge' by default
Use '--net' to attach a container to a network 

    docker run --net=host -it ubuntu /bin/bash

Inspect the network

    docker network inspect id|name

Inspect the IP address of a container

    docker inspect id|name
    docker inspect --format='{{.NetworkSettings.IPAddress}}' id|name

## CaaS (Container as a service) Exposing and connecting to container services

### Publishing a containers port
Use the `-p` option

    -p <hostPort>:<containerPort>
    -p <containerPort>
    -p <ip>:<hostPort>:<containerPort>
    -p <ip>::<containerPort>

Example:

    docker run -d -p 80:80 apache2

__This did not work!! Could not connect to the web service!__  
Resolved: the container was running in an antlet. I was trying to connect from
my local LAN. Works from another antlet (Win). 
Need to create a bridged NIC

### NAT for containers
When a port is mapped to a container, docker automatically creates an iptables rule

    iptables -t nat -L -n

### Show the container port

    docker ps
    docker port id|name
    docker inspect id|name

There are several places in the insplet json which displays the port

    docker inspect --format='{{.ExposedPorts}}' id|name

## Binding a specific IP address
By default containers get bound to all interfaces on the host machine - 0.0.0.0
To use a specific IP address

    docker run -d -p x.x.x:x:x id|name
    docker run -d -p 192.168.1.73:80:80 apache2

This must be an address on the host machine. 

## Autogenerate Docker Host Port
If you need to start multiple containers with the same service, you can let docker
autogenerate a port mapping

    docker run -d -p 80 apache2
    docker run -d -p 192.168.1.73::80 apache2

Verify with

    docker ps
    docker inspect id|name
    iptables -t nat -L -n

## Port Binding w EXPOSE and -P
Gives the ability to embed the port details in the image so you can easily find
the port details.

Use the EXPOSE directive in the Dockerfile for building an image

    FROM ubuntu:18.04
    MAINTAINER Dr. Mario Kaack <mario@kaack.com>
    RUN apt update && apt install -y apache2 && apt clean
    EXPOSE 80
    ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

Build the image

    docker build -t myapache2 .

Now you can inspect the image and look for the 'ExposedPorts' field fo 'Config

    docker inspect myapache2
    docker inspect --format='{{.Config.ExposedPorts}}' myapache2

Use -P in the 'docker run' command to autogenerate port bindings to those ports
declared with EXPOSE.

    docker run -d -P myapache2

You cannot fine tune the bindings with the -P option.. it takes no arguments
But you can still use the -p option if needed.

