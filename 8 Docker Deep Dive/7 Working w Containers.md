# Working with Containers

Containers are `Ephemeral` and 'Immutable`

    docker port <container>

## Logging

### daemon logs
/var/log/messages

### container/app logs
default app goes to STDOUT STDERR

Can set default logging driver in `daemon.json`
  - syslog, Splunk, Fluentd...
  - override per-container with
    - --log-driver  --log-opts

Inspect logs w

    docker logs <id|name>