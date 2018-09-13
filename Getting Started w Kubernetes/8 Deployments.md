# Kubernetes Deployments
## Rolling updates and Simple Rollbacks
### Deployment
_Deployments_ manage _Replica Sets_  
_Replica Sets_ manage _Pods_  

    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: hello-deploy
    spec:
      replicas: 10
      template:
        metadata:
          labels:
            app: hello-world
        spec:
          containers:
          - name: hello-pod
            image: nigelpoilton/plualsight-docker-ci:latest
            ports:
            - containerPort: 8080

Deploy

    kubectl create -f deploy.yml
    kubectl describe deploy hello-deploy
    kubectl get rs
    kubectl describe rs

rs is : replica set

### Updates
Edit the deploy.yml

      kubectl apply -f deploy.yml --record
      kubectl rollout status deployment hello-deployment
      kubectl get deploy hello-deploy
      kubectl rollout history deployment hello-deployment

--record allows the history to be recorded - recommended

    kubectl rollout undo deployment hello-deploy --to-revision=1