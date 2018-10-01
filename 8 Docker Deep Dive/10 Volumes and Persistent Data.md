# Volumes and Persistant Data

## Volume storage

    docker volume ls
    docker volume create myvol
    docker volume inspect myvol
    docker volume rm myvol
    /var/lib/docker/volumes/

### Attach to a container

    docker container run -dit --name voltest --mount source=myvol,target=/vol alpine sleep 1d
