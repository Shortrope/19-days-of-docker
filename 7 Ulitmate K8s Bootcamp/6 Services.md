# Services
External Access to Services  
Service Descovery  
Service to Service communication  

Service Spec  
File _vote-svc.yml

    apiVersion: v1
    kind: Service
    metadata:
      name: vote
      labels:
        role: vote
        version: v1
    spec:
      clusterIP:
      externalIPs:
      externalName:
      loadBalancerIP:
      loadBalancerSourceRanges:
      ports:
        - port: 80
          targetPort: 80
          nodePort: 30000
      selector:
        role: vote
        version: v1
      type: NodePort

`nodePort` is the external port

    http://<nodeIP>:<nodePort>

## Service Discovery
Service to service communication
This file is a _Deployment_
    apiVersion: v1
    kind: Service
    metadata:
      name: redis
      labels:
        app: redis
    spec:
      type: ClusterIP
      ports:
      - name: redis
        port: 6379
        targetPort: redis
      selector:
        app: redis
        role: master

Gets a new _ClusterIP_ that is pingable  

    kubectl get svc
    kubectl describe svc redis

You can ping 'redis' by name, from a 'vote' pod  

    kubectl exec -it vote-sckxk sh
    ping redis

### Not getting endpoints ^^