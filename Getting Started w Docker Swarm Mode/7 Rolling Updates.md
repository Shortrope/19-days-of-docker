# Rolling Updates

    docker service update --image web:v2 web

Some options

    --update-deley=20s web
    --update-parallelism=2 web

`watch`

    watch docker service ls
    watch docker service ps web

If you inspect the service you can view the update config

    "UpdateConfig": {
        "Parallelism": 1,
        "FailureAction": "pause",
        "Monitor": 5000000000,
        "MaxFailureRatio": 0,
        "Order": "stop-first"
    },

## Rolling Back
The 'inspect' will show the 'PreviousSpec' .. `--rollback` will rollback to that spec  

    docker service update --rollback web

`--force` ?? (18)

Inspect .UpdateStatus (19)
