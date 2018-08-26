# Chap 3

## 3. Building Images

Docker's Image building system  

    docker build -t imagename:tagname .
    docker build -t imagename:tagname Dockerfile

### Dockerfile syntax
    # Comment  
    INSTRUCTION arguments

- a comment '`#`' must be the first char on the line. no preceeding wht space

Dockerfile build instructions  

FROM ubuntu:16.04  
MAINTAINER Mario Kaack <mkaack@hotmail.com>  
COPY src dst
- copy a directory
  - COPY html /var/www/html
- copy files
  - COPY index.html contact.html /var/www/html/

ADD src dst 
- like COPY but can extract tar files and put each in its path
- can also ADD remote URLs

ENV key value
- Set environment variable

Syntax

    ENV key1=val1 var2=val2
Example

    ENV var1=ping var2=8.8.8.8.
    CMD $var1 $var2

ARG: <variable[=<default value>]
- Build argument <variable[=<default value>] (p.59)

USER <uid>|<uname>
- Start up user

WORKDIR /var/www/html
- Change the working directory. Will create the path it not exist

VOLUME ["/mnt/data", "/var/log/html"]  
VOLUME /mnt/data
- creates a dir which can be used to mount volumes from the host or other containers
- can be an array of paths or a single mountpoint

EXPOSE 53/udp 8080
- open network port

LABEL version="2.0"  
      release="20180805"
- add key/value pairs as metadata to your container
- label schema to avoid conflicts.. see p.63

RUN cmd arg1 arg2 ...
  - RUN commands **run at build time**
    - CMD commands run at run time
  - uses /bin/sh -c
  - Best practice to RUN all commands with one RUN
      - Each RUN command creates a new layer
  - Can use json array type
    - RUN ["bash", "-c", "rm", "-rf", "/tmp/asdf"]
    - the container does not require a shell to run the command
  - Install apache2 package
    - RUN apt update && \
          apt install -y apapch2 && \
          apt-get clean

CMD cmd
  - CMD commands are **run when the container is launched**
    - RUN commands run at build time
  - Only the last CMD will be run
  - executed using `/bin/sh -c <command>`
  - generally used to launch the app/service
  - can be owerridden at run-time with `docker run <command>`
  - If an ENTRYPOINT, then CMD is arguments to the ENTRYPOINT

ENTRYPOINT cmd
  - default application to run in the container
  - cannot be owerridden at run-time with `docker run <command>`
  - the commands at the end of `docker run` are used as arguments to the ENTRYPOINT
  - once the application terminates the container terminiates
  - see p. 68

HEALTHCHECK [options] CMD <command>
  - the command is run every 30 seconds by default
  - if command has exit code 0 then healthy, exit code 1 then unhealthy
  - options: --interval=30s, --timeout=30s, --retries=3
  - Example:
      HEALTHCHECK --interval=5m --timeout=3s
        CMD curl -f http://localhost/ || exit 1
  - Turn off healthcheck
      HEALTHCHECK NONE

ONBUILD  
STOPSIGNAL  
SHELL ["<shell>", "arg-1", "arg-n"]
- change the default shell

### .dockerignore
Exclude directories and files

    .git
    *.tmp

### Docker Image management
You can view the layers implemented on an image with

    docker history IMAGE_NAME

### Dockerfile Best Practices
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

