# Application Delployments and Updates
## Deployments
Gives you an update strategy

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: vote
      namespace: instavote
    spec:
      replicas: 8
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 2
          maxUnavailable: 1
      revisionHistoryLimit: 4
      paused: false
      minReadySeconds: 10
      selector:
        matchLabels:
          role: vote
        matchExpressions:
          - {key: version, operator: In, values: [v1, v2, v3]}
      template:
        metadata:
          name: vote
          labels:
            app: python
            role: vote
            version: v1
        spec:
          containers:
            - name: app
              image: schoolofdevops/vote:v1
              ports:
              - containerPort: 80
              protocol: TCP

Get update status and Rollback 

    kubectl rollout status deploy/vote
    kubectl rollout history deploy/vote
    kubectl rollout history deploy/vote --revision=3
    kubectl rollout undo deploy/vote --to-revision=2
  