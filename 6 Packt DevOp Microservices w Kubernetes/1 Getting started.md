# Getting started with Kubernetes
## 1.2 Setting up Minikube
[Minikube Download](https://github.com/kubernetes/minikube)

    minikube start --vm-driver=virtualbox
    minikube status
    minikube stop
    minikube delete

`minikube stop` does not delete any thing. When you start again it will be where you left it.  
`minikube delete` will reset the cluster  

### Minikube Add-Ons
Enabled by default:
- DNS
- Dashboard
- Storage provisioner

Useful to enable:
- Ingress:  
handles incoming http traffic
- Heapster:  
collects resourse utilization metrics

#### Enable add-ons
` minikube addons enable`

    minikube addons enable ingress
    minikube addons enable heapster

## 1.3 Deploying a Microservice

### Pods
The Pod is the Basic Deployment Unit
- A Pod can contain multiple containers - but seldom more than 1 or 2
    - Regular Docker containers
    - Can be _rkt_ or _CRIO_ containers  
- Scheduled on one _Node_

### Node
Just a Server
- Individual server - virtualized or bare metal
- Runs Docker engine
- Pods/containers started/scheduled by Kubernetes

### Namespaces
Resource Grouping and Isolation
- Groups of resourses - like Pods
- Default K8s resorces:
    - kube-system  
      system resources and should not be changed
    - default  
      Starts out empty

### Defining a Pod
[Documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/)  
Use `kubectl` to list existing Pods

    kubectl get pods

Resources are defined in YAML files  
Define a Pod with a single container  
_pod.yml_  

    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod
      namespace: default
    spec:
      containers:
      - name: service
        image: nginx
        ports:
          - containerPort: 80
        env:
          - name: SOME_ENV_VAR
            value: Hello World

Apply the .yml file

    kubectl apply -f pod.yml
    kubectl get pods

You can edit this same file and re-apply to implement the changes

At this point you have a running _container_ in a _Pod_ in a _Node_ in a K8s _Cluster_  
Open issues  
- No network accessability

### 1.4 Service Resiliency and Scalability
**Pod Limitations**  
- Each Pod is assigned to a specific node in the cluster
- If a Pod crashes, it will be restarted
- If a Node crashes, the Pods on it will be lost

**A Single Pod**
- **Disposable**
- **Not resilient by itself**
- **Not scalable by itself**

High-level Controllers: Add _Resilientcy_ and _Scaleability_
- ReplicatSet
    - Manages Pods
    - Self-healing and scalable
- StatefulSet
    - Similar to ReplicaSet
    - Pods have stable network identity

**Never manually create a Pod - Rely on controllers to manage Pods for you:**
- ReplicaSet
- Deployment
- StatefulSet

