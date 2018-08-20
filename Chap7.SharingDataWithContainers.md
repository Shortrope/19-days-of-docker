# Chap 7. Sharing Data with Containers

## **Data Volume**
A Data Volume is a part of the Docker Host file system that gets mounted inside
the container The Data Volume is not part of the container file system

    /var/lib/docker/volumes/`<id>`/_data/  

You can create a Volume with a Docker file or with the docker run -v option

    FROM ubuntu:16.04
    VOLUME /mountpointdemo
or

    docker run -v /mountpointdemo

You can look for Volume info in an image. If the image was created with a VOLUME in the docker file.

    docker inspect IMAGE_NAME

After starting a container from the image inspect the image with

    docker inspect -f '{{json .Mounts}}' id|name

If you rm the container the volume remains in /var/lib/docker/volumes/`<id>`/
You can remove the volume when you rm the container

    docker rm -v id|name

_**Example:**_

    FROM ubuntu:16.04
    VOLUME /mountpointdemo

Build the image

    docker build -t mountpointdemo .

Launch a container

    docker run --rm -it mountpointdemo

In the container create a file in /mountdir

    touch /mountdir/I-was-hear

Then in the host OS check

    /var/lib/docker/volumes/`<id>`/_data/  

and you will see your file.  

## **The `volume` command**
The `docker volume` command has four sub commands

- ls
- inspect
- create
- rm

Create a volume with:

    docker volume create --name mysqldatavol


## **Sharing Host Data**
You can mount  a host directory of file to a container's data volume during container launch (but
not during build with a Dockerfile) with
the `-v` option.  
The `-v` option has five formats

- `-v <container mount path>`
- `-v <host path>:<container mount path>`
- `-v <host path>:<container mount path>:<read write mode>`
- `-v <volume name>:<container mount path>`
- `-v <volume name>:<container mount path>:<read write mode>`

`<host path>` is an absolute path in the docker host
`<container mount path>` is an absolute path in the container
`<read write mode>` can be either `ro` or `rw`
`<volume name>` is the name of a volume created with `docker volume create`

Create a volume and mount it in a container:

    docker volume create --name myvolume
    docker run -v myvolume:/myvol -it ubuntu

Mount a  local directory to a mountpoint in a container:

    docker run -v /tmp/mydir:/mydir -it ubuntu

Inspect a containers mounts

    docker inspect --format='{{json .Mounts}}' id|name

## **Sharing Data between Containers**
The `--volumes-from` option takes a container name or id and automatically mounts all the data
volumes from that container in this newly created container.  
You can also mount multiple container volumes  

Create a data container (a data only container) and mount its volumes in a new container

    docker run -v /data --name datacontainer busybox /bin/true
    docker run --volumes-from datacontainer -it ubuntu /bin/bash

## **Common Pitfalls**
### Directory Leaks
Auto-generated directories are not auto-deleted when a container is rm'ed.  
Use `-v` to remove the volume with the container  

    docker rm -v id|name

- Undeleted directories: can grow  
- Third party images: may have been built with a VOLUME instruction

Once the container is removed, there is not way to identify which directories do not have a 
container assigned.
### Avoid Directory Leaks
- Always inspect docker images for data volumes in the image
- Always run `docker rm` with the -v option. The volume will only be deleted if no other containers are attached
- Implement an audit framework to find dir's w/out a container assosication

Never use a data volume as a storage during the build process
