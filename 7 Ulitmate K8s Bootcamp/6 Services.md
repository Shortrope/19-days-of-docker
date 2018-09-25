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