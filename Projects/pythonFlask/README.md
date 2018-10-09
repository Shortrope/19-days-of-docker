# README

## Dockerfile
This COPY's the app for deployment

    docker run -d --name pyflask shortrope/pyflask:latest

## Dockerfile-dev
This exposes the /app VOLUME for editing  
Run command

    docker run -v E:\_Projects\100\19-days-of-docker\Projects\pythonFlask\app:/app -p 5000:5000 -it --name pyfdev pyflask:1.0 /bin/sh

 Start the app: 
 
    python3 /app/app.py