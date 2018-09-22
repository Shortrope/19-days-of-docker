# Ingress Routing and Publishing Ports

Ingress overlay network: sits between the _Nodes_ and the _Containers_  

Add a load balancer outside the Nodes.  (4)  
  HA Proxy  
  Nginx  

The publish mode = `ingress` if publishing to the _Swarm_ - the default.

    root@dm1:~# docker network ls
      NETWORK ID          NAME                DRIVER              SCOPE
      adb8246f899b        bridge              bridge              local
      df0bdff49efd        docker_gwbridge     bridge              local
      59b03541f539        host                host                local
      uplld7rfqa6t        ingress             overlay             swarm
      cda9117332ac        none                null                local

Inspect the _ingress_ network to view its IP range and gateway address

    docker network inspect ingress

You can publish to _Host_ instead of the _Swarm_  
The publish mode = `host` if publishing to a specfic _Host_   - For access to a specific container (5,6,7)  

    docker service update --publish-rm 80 web
    docker service update --publish-add mode=host,published=8081,target=80 web

- Do not use for a container with multiple intances on a single node  
- Good for use w a _Global mode_ container  

Commands

    docker service update --publish-rm 8080 web
    docker service update --publish-add mode=host,published=8080,target=80 web
    docker service inspect web  

In the `inspect` command look for
- PreviousSpec.EndpointSpec.Ports.PublishMode
- Spec.TaskTemplate.ContainerSpec.Endpoint.Spec.Ports.PublishMode

Automatic creatation of published port by not providing the published port

    docker service create --name web -p target=80 nginx
    docker serivice inspect web --pretty    // Ports.PublishedPort

At this point we have no Load Balancing of incoming packets to the _Nodes_
