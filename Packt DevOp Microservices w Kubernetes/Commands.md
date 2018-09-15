    minikube start --vm-driver=virtualbox
    minikube status
    minikube stop
    minikube delete

    minikube addons enable ingress
    minikube addons enable heapster

    kubectl get pods
    kubectl apply -f pod.yml