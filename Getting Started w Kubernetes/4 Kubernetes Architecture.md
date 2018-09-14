https://github.com/kubernetes/kubernetes

# Architecture
- Runs on Linux


## Masters
- Keep nodes off of Masters
- Kube-apiserver
  - Front-end to  teh control plane
  - Exposes the API (REST)
  - Consumes json .. via manifest files

- Cluster store
  - Persistent storage
  - Cluster state and config
  - Uses etcd
  - Distributed, consistend, watchable
  - **The "Source of Truth" for the cluster**
  - **Have a backup plan for it**

- kube-controller-manager 
  - Controller of controllers
    - Node controller
    - Endpoints controller
    - Namespace controller
    - ...
  - Watches for changes
  - Helps maintain _desired state_

- kube-scheduler
  - Watches _apiserver_ for new pods
  - Assigns work to nodes
    - affinity/anti-affinity
    - constraints
    - resources
    - ...

## Nodes
a.k.a "Minions"

1. Kubelet  
Main Kubernetes agent
    - Registers node with cluster
    - Watches apiserver
    - Instantiates _pods_
    - Reports back to _master_
    - Exposes endpoint on :10255
      - /spec
      - /healthz
      - /pods

2. Container Engine  
Does Container management
    - Pulling images
    - Starting/stopping containers
    - Pluggable
      - Usually _Docker_
      - Can be _rkt_ (coreOS rocket)

3. kube-proxy  
Kubernetes networking
    - Pod IP addresses
      - All containers in a pod share a single IP
    - Load balances across all pods in a _service_


## Pods
Containers always run inside of pods!!  
Pods can have multiple containers  
Scaling means adding Pods, not containers  

Lifecycle:
- pending -> Running -> succeded/failed

## Services
Stable networking  
Load balancer  
provides same IP  
provides dns  
### Labels
very powerful  
Load balances based on labels  


## Deployments - Replication Controllers
Helps us manage Pods  
Scale Podd  
Desired state  
Rolling updates/rollbacks  

