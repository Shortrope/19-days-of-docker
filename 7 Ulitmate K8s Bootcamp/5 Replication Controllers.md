# Replication Controllers
When Pods die they do not come back they are gone.
ReplicaSets provide 
- fault tolerance
- self healing

Commands

    kubectl config set-context $(kubectl config current-context) --namespace=instavote
    kubectl config view
    kubectl config current-context
    kubectl get ns
    kubectl get rs
    kubectl describe rs


## Namespace and Switching Context

Create a Namespace for your project
File: _instavote-ns.yml_

    apiVersion: v1
    kind: Namespace
    metadata:
      name: instavote

List Namespaces

    kubectl get ns

- default
- kube-public
- kube-system

Which Namespace are you connected to?

    kubectl config view
    kubectl config current-context

Switch Namespace

    kubectl config set-context $(kubectl config current-context) --namespace=instavote

After swiching Namespace you only see info for that Namespace when running commands

## ReplicaSet Spec
Check out _matchLabels_ and _matchExpression_

    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
      name: vote
    spec:
      replicas: 5
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

Show Labels

    kubectl get pods --show-labels

Show ReplicaSets

    kubectl get rs
    kubectl describe rs
