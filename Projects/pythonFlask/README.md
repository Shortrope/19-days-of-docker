# README

## Dockerfile-base
- Base image the _dev_ and _prod_ images are built from.
- Installs Python and Flask on an alpine image

## Dockerfile-dev
This build exposes
- port 5000
- the `/app` VOLUME for editing  

Start the container with the following `docker run` command:

    docker run -v E:\_Projects\100\19-days-of-docker\Projects\pythonFlask\app:/app -p 5000:5000 -it --name pyfdev pyflask-dev:1.0 /bin/sh
Start the app from the containers command line, with:

    python3 /app/app.py


## Dockerfile-prod

- This build COPY's the app for deployment
- EXPOSE's port 5000
- Does NOT expose the /app VOLUME

Start the container with the following `docker run` command:

    docker run -d --name pyflask shortrope/pyflask:latest
