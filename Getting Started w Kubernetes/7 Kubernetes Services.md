# Kubernetes Services

How do we access our app

Services:
- REST objects in the K8s API
- Abstraction
- Provides Reliable Network Endpoint - IP, DNS, Ports to client

Also get an `Endpoint` service
- has the list of nodes and pods

Labels
- Sticks the pods to the service

Service Dicovery
- DNS based (best)
- Environment variables

## Createing a Service the Iterative way
_Don't do this way... use .yml file... declaritive way_

    kubectl expose rc hello-rc --name=helool-svc --target-port=8080 --type=NodePort  
    kubectl describe svc hello-svc
    kubectl delete  svc hello-rc 

shows the cluster IP and port

## Createing a Service the Declaritive way
