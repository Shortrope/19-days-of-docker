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

If error:

    kubectl get pods -o wide
    kubectl get pods vote -o yaml    // look at status section
    kubectl describe pods vote

