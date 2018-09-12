# Installing Kubernetes

## Manual Install
**kubeadm**

### Every node (master and minion) requires:
- Docker (or rkt)
- Kubelet:  Node agent
- Kubeadm:  Tool to build the cluster
- Kubectl:  kubernetes client
- CNI:  CNI Networking

#### Node 1

    apt-get update && apt-get install -y apt-transport-https
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
    deb http://apt.kubernetes.io/ kubernetes-xenial main
    EOF
    apt-get update
    
    https://git.io/weave-kube-1.6