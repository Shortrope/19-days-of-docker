# Working w Pods

## Pod Theory
has 1 or more container  
Send manifest file to api server  
Single IP to one Pod  
Inter pod communication  
Intra pod communication: via local host  
Pods: Atomic Deployment  

### Lifecycle
Manifest is sent to apiserver
Pod is spun up on a node
Pending until all containers are up and running  
Running  
Succeeded or Failed  

Each Pod is Totally replacable


## Deploying your First Pod

pod.yml

    apiVersion: v1
    kind: Pod
    metadata:
      name: hello-pod
      labels:
        zone: prod
        version: v1
    spec:
      containers:
      - name: hello-ctr
        image: nigelpoulton/pluralsight-docker-ci:latest
        ports:
        - containerPort: 8080

kubectl create -f pod.yml  
kubectl get pods  
kubectl get pods/hello-pod
kubectl get pods --all-namespaces
kubectl describe pods
kubectl delete pods hello-pod

**You will normally be working with a _Replication Controller_**
Implements desired state

rc.yml

    apiVersion: v1
    kind: ReplicationController
    metadata:
      name: hello-rc
    spec:
      replicas: 10
      selector:
        app: hello-world
      template:
        metadata:
          labels:
            app: hello-world
        spec:
          containers:
          - name: hello-pod
            image: nigelpoulton/pluralsight-docker-ci:latest
            ports:
            - containerPort: 8080

kubectl create -f rc.yml  
kubectl get rc  
kubectl describe rc  
_edit rc.yml_  
kubectl aplly -f rc.yml  


