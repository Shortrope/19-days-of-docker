    minikube start --vm-driver=virtualbox
    minikube status
    minikube stop
    minikube delete
    minikube addons list
    minikube addons enable ingress

    minikube addons enable ingress
    minikube addons enable heapster

    kubectl get pods
    kubectl apply -f pod.yml
    kubectl delete -f pod.yml

    kubectl apply -f my-service_replicaset.yml
    kubectl scale replicaset my-service --replicas=8
    kubectl delete -f my-service_replicaset.yml

    kubectl apply -f my-deployment.yml
    kubectl get replicasets
    kubectl get pods
    kubectl edit deployment my-deployment
    kubectl rollout undo deployment/my-deployment


    my-service.default.svc.cluster.local
