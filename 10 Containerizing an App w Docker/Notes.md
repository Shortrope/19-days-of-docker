# Containerizing an App with Docker

    docker container commit 
    docker container export -o filename.tar id|name
    docker image import file|url image_name:tag

## Dockerfile

### FROM
- must be first instruction
- Keywork 'scratch' indicates build with not base image

### ENV

    ENV <variable> <value>
    ENV <variable=value>

- It declares an environment variable
- The variable and it value persist into derived containers

Two ways to declare multiple ENV vars:

    ENV MONGO_MAJOR 3.4
    ENV MONGO_VERSION 3.4.4
    ENV MONGO_PACKAGE mongodb-org
Or with a single instruction:

    ENV MONGO_MAJOR=3.4 \
        MONGO_VERSION=3.4.4 \
        MONGO_PACKAGE=mongodb-org

### ARG

    ARG <variable[=default_value]>

- for args passed on the command line with `--build-arg=`
- ARG can optionally define a default value.. unlike ENV
- ARG vars do not persist into the derived container
- Altered build args break build cache at the point it is consumed, not defined
- But, vars defined w ENV override vars defined w ARG.. a build arg can be passed on to the container

Example:

    ARG VERSION
    ENV VERSION=${VERSION:-3.5.1}