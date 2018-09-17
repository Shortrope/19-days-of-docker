# Installation

[Installation from the Kubernetes website](https://kubernetes.io/docs/setup/independent/install-kubeadm/)

1. Hardware requirements
    - 2 CPUs (Master)
    - 2G RAM per node
    - Full network connectivity between Nodes

1. Make sure no swap  
    - Comment the 'swap' line in `/etc/fstab`
1. MAC address and product_uuid are unique on each node.  
    <pre>cat /sys/class/dmi/id/product_uuid</pre>
1. Install Docker 17.03  
    <pre>apt-get update
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
    add-apt-repository "deb https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"
    apt-get update && apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')</pre>
1. Install kubeadm, kubelet and kubectl  
    <pre>apt-get update && apt-get install -y apt-transport-https curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
    deb http://apt.kubernetes.io/ kubernetes-xenial main
    EOF
    apt-get update
    apt-get install -y kubelet kubeadm kubectl
    apt-mark hold kubelet kubeadm kubectl</pre>


    Checks

        docker version
        kubectl version
        kubeadm version
        kubelet --version


    Upgrade with 
    
        apt update && apt upgrade

## Initializing the Master

    hostname -i
    kubeadm init --apiserver-advertise-address 192.168.1.20 --pod-network-cidr=172.17.0.0/16

The end of the initialization has some instructions

    Your Kubernetes master has initialized successfully!

    To start using your cluster, you need to run the following as a regular user:

    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    You should now deploy a pod network to the cluster.
    Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
    https://kubernetes.io/docs/concepts/cluster-administration/addons/

    You can now join any number of machines by running the following on each node
    as root:

    kubeadm join 192.168.1.20:6443 --token f1mtka.xqu54c79zzrwsgk2 --discovery-token-ca-cert-hash sha256:7d6df3a302450b2bf2647b954330de26e972a003545a737f4e61937b
    4d3768ae


Run the `kubeadm join ..` command on the other nodes to join the cluster  
Enable `kubectl` by creating the `~/.kube` directory and cp'ing the config file w the instructions given.  
Check `kubectl` works and the nodes in the cluster with:  

    kubectl get nodes

Output:

    NAME      STATUS     ROLES     AGE       VERSION
    kubm1     NotReady   master    27m       v1.11.3
    minion1   NotReady   <none>    15m       v1.11.3
    minion2   NotReady   <none>    14m       v1.11.3

Other versions of `kubectl get ...`

    kubectl get nodes -o wide
    kubctl get nodes,pods --all-namespaces -o wide
Watch for changes in the command (update every 1 second)

    watch -n 1 kubectl get nodes,pods




## Set up CNI - Container Network Interface (Weave Net)
Nodes are not ready because there is no cluster network setup yet  
This is so the pods can communicate across nodes

    export kubever=$(kubectl version | base64 | tr -d '\n')
    kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$kubever"

Check with

    kubectl get nodes -o wide
    kubectl cluster-info
    kubectl cluster-info dump > cluster-info-dump
    kubectl get cs
    kubectl get events

cs - componentStatus


[Choose a Pod Network add-on](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#initializing-your-master)