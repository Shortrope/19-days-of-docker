# Health Checks

    version: '3.7'
    service:
      image: xxxx
      ports:
        -7000:80
      healthcheck:
        test: curl ... || exit 1
        interval: 1m30s
        timeout: 30s
        retries: 3
      

IF exit code of the 'test' command is non-zero

Bakeing healthcheck into the image w a Build file

    FROM swarmgs/cowsay
    HEALTHCHECK --interval=5s CMD /usr/games/fortune || exit 1

Turn off Healthcheck if it is baked into the image

    docker run --no-healthcheck
    docker service create --no-healthcheck

and in a compose file

    healthcheck:
      disable: true
