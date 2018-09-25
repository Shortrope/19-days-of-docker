# Pods
Pod Spec:  
https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.11/#pod-v1-core  

Should only create Pods with a Controller: Deployment, StatefulSet, Job

ContainerSpec:  
- Image  
- Ports  
- Volumes  
- Environment  

Get info about properties

    kubectl explain pods

Example Pod:   
File: _vote-pod.yml_

  
    apiVersion: v1
    kind: Pod
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

Launch the Pod and check status

    kubectl apply -f vote-pod.yml
    kubectl get pods -o wide
    kubectl get pods vote -o yaml    // get status
    kubectl describe pods vote
    kubectl logs vote -f
    kubectl exec -it vote sh
    kubectl port-forward pod/vote 8080:80
    kubectl edit pods vote 

## Trouble Shooting
If error:

    kubectl get pods -o wide
    kubectl get pods vote -o yaml    // look at status section
    kubectl describe pods vote

## Attaching a Volume
Create a Volume and a volumeMount point  
Volume only live on the Node the container lives on.  
After deleting the pod the volume remains

Create a Database pod  
File: _db-pod.yml

    apiVersion: v1
    kind: Pod
    metadata:
      name: db
      labels:
        app: postgres
        role: database
        tier: back
    spec:
      containers:
        - name: db
          image: postres:9.4
          ports:
            - containerPort:5432
          volumeMounts:
            - name: pg-data
            - mountPath: /var/lib/postgresql/data
      volumes:
      - name: pg-data
        hostPath:
          path: /var/lib/postgres
          type: DirectoryOrCreate

Test w 

    kubectl apply -f db-pod.yml --dry-run

## Multi Container Pods
These two containers share the same data volume  
Also share the same hostnmae and IP  
File: _multi-container-pod.yml_

    apiVersion: v1
    kind: Pod
    metadata:
      - name: web
        labels:
          app: nginx
          role: ui
          tier: front
    spec:
      containers:
        - name: nginx
          image: nginx:stable-alpine
          ports:
            - containerPort: 80
              protocol: TCP
          volumeMounts:
            - name: data
              mountPath: /var/www/html-sample-app

        - name: sync
          image: schoolofdevops/sync:v2
          volumeMounts:
            - name: data
              mountPath: /var/www/app

      volumes:
        - name: data
          emptyDir: {}

The _emptyDir_ is not persistant!

## Connect to individual Containers
To connect to a specific container in a multi container pod  
use `-c <name>`

kubectl exec -it web sh -c sync
kubectl logs web -c sync

