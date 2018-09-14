# Kubernetes Docs
https://kubernetes.io/docs/home/?path=users&persona=app-developer&level=foundational


## Users > Cluster Operator > Foundational
1. Get an overview of K8s
    - What is Kubernetes?  
        Platform for managing containerized workloads  
        Declarative configuration and automation  
        It orchestrates based on user workload  
            - Computing  
            - Networking  
            - Storage  
        Portable Cloud Platform

### Node
A _Node_ is a worker machine  
A Node runs _Pods_  
Nodes are managed by _Master_ components  

#### Node status
- Addresses
- Condition
- Capacity
- Info

Addresses: 
- Hostname:  
    Hostname of the node. Can be overridden with the kubelet `--hostname-override` parameter
- ExternalIP:  
    IP address of the Node. Externally available and routable
- InternalIP:  
    IP address of the node, used only within the cluster

Condition:  
The `conditions` field describes the status of all `Running` nodes
- OutOfDisk
- Ready: if the Node is healthy and ready to accept pods
- MemoryPressure:  Mem running low
- PIDPressure
- DiskPressuer
- NetworkUnavailable
- ConfigOK

Represented as a JSON object

    "conditions": [
      {
        "type": "Ready",
        "status": "True"
      }
    ]

https://kubernetes.io/docs/concepts/architecture/nodes/