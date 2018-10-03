Sept 2017
# Docker Certified Associate Study Guide: Check List

- Experience with Linux and /or Windows server
- Exposure to Docker Enterprise Edition
- Experience with container security
- Experience with at least 1 cloud provider
- Understanding of Docker Best Practices
- Experience with configuration management tools

## Exam Categories:
- Orchestration
- Image Creation, Management and Registry
- Installation and Configuration
- Networking
- Security
- Storage and Volumes

## Definitions
**UCP: Universal Control Plane**  
The enterprise-grade cluster management solution from Docker. You install it on-premises or in your virtual private cloud, and it helps you manage your Docker swarm and applications through a single interface.  
**DTR: Docker Trusted Registry**  
A containerized application that runs on a swarm managed by Docker Universal Control Plane (UCP). It can be installed on-premises or on a cloud infrastructure.  


## Image Creation, Management, and Registry (20%)
<input type="checkbox"> Use CLI commands such as list, delete, prune, rmi, ... to manage images  
<input type="checkbox"> Show the main parts of a Dockerfile  
<input type="checkbox"> Describe Dockerfile options - add, copy, volumes, expose, entrypoint, ...)  
<input type="checkbox"> Demonstrate tagging an image  
<input type="checkbox"> Inspect images and report specific attribs using filter and format  
<input type="checkbox"> Describe how image layers work  
<input type="checkbox"> Display layers of a Docker image  
<input type="checkbox"> Give examples on how to create an efficient image via a Dockerfile  
<input type="checkbox"> Modify an image to a single layer  
<input type="checkbox"> Utilize a registry to store an image  
<input type="checkbox"> apply a file to create a Docker image ??  


### Registry
- Deploy a registry (not architect)
- Configure a registry
- Log into a registry
- Utilize search in a registry
- Push an image to a registry
- Sign an image in a registry
- Pull an image from a registry
- Describe how image deletion works
- Delete an image from a registry

## Networking (15%)
- Create a Docker bridge network for a developer to use for their containers
- Describe the different types and use cases for the built-in network drivers
- Publish a port so that an application is accessible externally
- Identify which IP and port a continer is externally accessible on
- Describe the difference between "host" and "ingress" port publishing mode
- TShout container and engine logs to understand a connectivity issue between containers
- Deploy a service on a Docker overlay network
- Understand the Container Network Model and how it interfaces with the Docker engine and network and IPAM drivers
- Configure docker to use external DNS
- Use Docker to load balance http/https traffic to an application (Configure L7 load balancing w Docker EE)
- Understand and describe the types of traffic that flow between the Docker engine, registry, and UCP controllers

## Storage and Volumes (10%)
- State which graph driver should be used on which OS
- Demonstrate how to configure devicemapper
- Compare object storage to block storage and explain which one is preferable when available
- Describe how volumes are used with Docker for persistent storage
- Summerarize how an application is composed of layers and where those layers reside on the filesystem
- Identify the steps you would take to clean up unused images on a filesystem and on DTR
- Demonstrate how storage can be used across cluster nodes

## Orchestration (25%)
- Complete the Setup of a Swarm Mode cluster w managers and worker nodes
- State the differences between running a container vs running a service
- Demonstrate steps to lock a swarm cluster
- Extend teh instructions to run individual containers into running services under swarm
- Interpret the output of "docker inspect" commands
- Convert an application deployment into a stack file using a Yaml compose file w "docker stack deploy"
- Manipulate a running stack of services
- Increase # of replicas
- Add networks, publish ports
- Mount volumes
- Illustrate running a replicated vs global service
- Identify the steps needed to troubleshoot a service not deploying
- Apply node labels to demonstrate placement of tasks
- Sketch how a Dockerized application communicates with legacy systems
- Paraphrase the importance of quorum in a swarm cluster
- Demonstrate the usage of templates with "docker service create"

## Securtiy (15%)
- Describe the process of signing an image
- Demonstrate that an image passes a security scan
- Enable Docker Content Trust
- Configure RBAC in UCP
- Integrate UCP w LDAP/AD
- Demonstrate creation of UCP client bundles
- Describe default engine security
- Describe swarm default security
- Describe MTLS
- Identity roles Describe the difference between UCP workers and managers
- Describe process to use external certificates w UCP and DTR

## Installation and Configuratioin (15%)
- Upgrade the Docker engine
- Setup of Repo, Select a storage driver, and complete installation of Docker Engine on multiple platforms
- Configure Logging drivers (splunk, journald, ..)
- Setup Swarm, config Managers, add Nodes, setup Backup schedule
- Create and manage User and Teams
- Interpret Errors to trouble shoot installation issues 
- Outline the sizing requirements prior to installation
- Understand Namespaces, Cgroups, and configuration of certificates
- Use certificate-based client-server authenticatioin to ensure a Docker daemon has the rights to access images on a registry
- Consistently repeat steps to deploy Docker engine, UCP, and DTR on AWS and on Premises in an HA config
- Complete configuration of Backups for UCP and DTR
- Configure the Docker daemon to start on boot

