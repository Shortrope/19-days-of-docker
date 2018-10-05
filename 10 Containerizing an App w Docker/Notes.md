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

### RUN
Allows you to create or retrieve remote content to the image  
Executes commands and thier arguments inside the container  
Two syntax forms:  
- shell
    - most common
    - just supply the command and arguments
    - uses the existing shell and therefore can use the shells capabilities
- exec
    - usually used when the filesystem does not have a shell
    - uses json format and each part must be in "double quotes"

Examples:

    RUN <command param ...> 
    RUN <["executable", "param", ...]>

RUN always relies on the cache. If retrieving an external file(s), it may change from build to build but RUN will not accout for this and use the cache if available.  
You can instruct the build to bypass the cache

#### Best practice
Reduce number of layers

    RUN apt update
    RUN apt install -y wget
    Run rm -rf /var/lib/apt/lists/*
Vs

    RUN apt update \
        apt install -y wget \
        rm -rf /var/lib/apt/lists/*

### COPY
Add local build content - stored in the build context  
- RUN adds remote content  
- ADD is similar but older and recommended to use COPY instead  

COPY adds artifacts to a dest path in the image  
Multiple sources can be specified on the same cmd to a single dest  
Sources can use globbing chars (conform to golang filepath.match)  
Dest can be relative or absolute path in the image  
Content is added w a UID and GID of 0  

    COPY <src> ... <dst>
    COPY ["<src>" ... "<dst>"]
    COPY foo /bar
    COPY foo /bar/
    COPY foo bar        // copied relative to / or previous WORKDIR instruction

## Define what a container executes
Two instructions handle this
- CMD
- ENTRYPOINT

### CMD
- Used to defina a default command  
- Or default parameters to ENTRYPOINT  
    - must use exec syntax otherwise will attempt to run in a shell
- But can be overriden on the command line  
    - docker container run my-image other-cmd
- Two syntax forms
    - shell
    - exec (prefered)

Examples:

    CMD <command parameter ...> 
    CMD <param param ...>
    CMD ["<command>", "<param>", ...]

## ENTRYPOINT
- Used for defining a specific executable
- Command line args are appended from the CMD instruction or the cli
- Two syntax forms
    - shell
    - exec (prefered)