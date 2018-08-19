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
### Installing docker compose  
https://github.com/docker/compose/releases/latest

    curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

Or Docker Compose can be installed as a Python package

    pip install -U docker-compose

Check the version

    docker-compose --version

### The docker-compose file
The default `docker-compose` file is 

    docker-compose.yml
    docker-compose.yaml

You can use the `-f` option to designate a different file

The format of the `docker-compose.yml` file

    version: "<version>"
      services:
        <service>:
          <key>: <value>
          <key>:
          - <value>
          - <value>

    networks:
      <network>:
        <key>: <value>

    volumes:
      <volume>:
        <key>: <value>

- `<version>` is the docker-compose file format version
- `<services>` ?? not sure ??
- `<key>` Many keys listed on p.179
  - image
  - build
  - command
  - deploy
  - depends-on
  - ...

### The `docker-compose` Command

|`docker-compose` options|Description|
|------|-----------|
| -f, --f `<file>` | Specifie an alternate file - other than docker-compose.yml |
| -p, --project-name `<name>`|specifie an alternate project name|
| --verbose| show more output|
|-v, --version| show version info and exit|
|-H, --host `<host>`| specify the daemon socket to connect to|
|-tls, --tlscacert, --tlskey, --skip-hostname-check| flags for Transport Layer Security - TLS|

|`docker-compose` commands|Description|
|------|-----------|
|build| builds or rebuilds services.|
|bundle| used to create a Docker bundle from the compose file, this is still an experimental feature on Docker 1.13.|
|config| command to validate and display the compose file.|
|create| creates the services defined in the compose file.|
|down| used to stop and remove containers and networks.|
|events| used to view the real-time container life cycle events.|
|exec| enables you to run a command in a running container. It is used predominantly for debugging purposes.|
|kill| kills running containers.|
|logs| displays the output from the containers.|
|pause| used to pause services.|
|port| prints the public port for a port binding.|
|ps| lists the containers.|
|pull| pulls the images from the repository.|
|push| pushes the images to the repository.|
|restart| used to restart the services defined in the compose file.|
|rm| removes the stopped containers.|
|run| runs a one-off command.|
|scale| sets a number of containers for a service.|
|start| starts services defined in the compose file.|
|stop| stops services.|
|unpause| used to unpause services.|
|up| creates and starts containers.|
|version| prints the version of Docker Compose.|

`docker-compose` commands must be run from the directory that contains the docker-compose.yml file
Each `docker-compose.yml` file is considered a project. The directory name is used by default as the
project name.

You `build` the images/services with

    docker-compose build

images from the repo

    docker-compose pull

Start the services/containers 

    docker-compose up

View the containers associated the this project

    docker-compose ps