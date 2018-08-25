# Command Reference
## Table of contents
- [docker](#docker)
- [docker image](#docker-image)
- [docker build](#docker-build)
- [docker run](#docker-run)
- [docker container](#docker-container)
- [docker commit](#docker-commit)
- [docker save](#docker-save)
- [docker stack](#docker-stack)
- [docker service](#docker-service)
- [docker inspect](#docker-inspect)
- [docker swarm](#docker-swarm)
- [docker top](#docker-top)
- [docker logs](#docker-logs)
- [Dockerfile Build Options](Dockerfile-Build-Options)

- [Misc](#Misc)

## docker 
`docker start`  
`docker stop`  
`docker restart`  
`docker pull`  

[toc](#Table-of-contents) 

## docker image
| Command  | Description |
|--------- |-------------|
|  build   | Build an image from a Dockerfile |
|  history | Show the history of an image |
|  import  | Import the contents from a tarball to create a filesystem image |
|  inspect | Display detailed information on one or more images |
|  load    | Load an image from a tar archive or STDIN |
|  ls      | List images |
|  prune   | Remove unused images |
|  pull    | Pull an image or a repository from a registry |
|  push    | Push an image or a repository to a registry |
|  rm      | Remove one or more images |
|  save    | Save one or more images to a tar archive (streamed to STDOUT by default) |
|  tag     | Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE |

[toc](#Table-of-contents) 
 
## docker build

[toc](#Table-of-contents)

## docker run
|Option|Description
|------|-----------|
| -d | detached mode |
| -i | interactive |
| -t | pseudo terminal |
| --name | name the container |
| -c | run a command |

[toc](#Table-of-contents)

## docker container

[toc](#Table-of-contents)

## docker commit

[toc](#Table-of-contents)

## docker save
Export an _image_ to a tarball

    docker save -o /tmp/fridge.tar fridge
    docker load /tmp/fridge.tar

`load` imports the image.  These two can be used to move an image to another host.

[toc](#Table-of-contents)

## docker stack

[toc](#Table-of-contents)

## docker service

[toc](#Table-of-contents)

## docker inspect

[toc](#Table-of-contents)

## docker swarm

[toc](#Table-of-contents)

## docker top

[toc](#Table-of-contents)

## docker logs

    docker logs -f d429e2a

-f  follow the log, like `tail` command

[toc](#Table-of-contents)

## Dockerfile Build Options

[toc](#Table-of-contents)

## Misc
### nsenter
If the process is not a shell, you can enter and start a shell  
Exiting will not stop the container
Here are three ways to do it:

    docker-enter f429a684b 
    docker exec -it f429a684b /bin/bash
    nsenter -m -u -n -p -i -t f429a684b /bin/bash


[toc](#Table-of-contents)