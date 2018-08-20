# To Do: Deliberate Practice/Performance

1. Create some Dockerfiles using commands in chap 3.
1. Build custom container
1. Publish image to Docker Hub

Which options use an '=' sign? or is it optional?


What images do I already have locally
Search for a image
Get an image
Download a specific version image
Remove an image
Run a container
  - in interactive mode
  - in daemon mode
  - detach / attach to a container
Manage containers
  - list all images
  - list all containers 
  - stop, start, restart a container
  - diff a container vs its image
  - remove a container
Create a new image from a container
View the history of an image

## Inspect: what are the important sections
- Image
- Container
- Volume

Is it worth using `--format=` vs just inspecting w `less`?

## Networking
- bridges
- Ports  
- IP addresses  

Create and use bridges
- Use the default bridge to communicate between containers
- Use the default bridge communicate w the containers from the host
- Use the default bridge communicate w the containers from a PC on the LAN
- Create user defined bridge to communicate between containers
- Create user defined bridge to communicate w the containers from the host
- Create user defined bridge to communicate w the containers from a PC on the LAN

Exposing Ports
- Hot to expose ports
- three ways to find the open ports
- view the iptables rules created when a port is exposed

Assign IP address

Set up networking in a Dockerfile
Set up networking with `docker run`

## Volumes
- Mount host directory  
- Mount a created volume  
- Mount another containers volume  
- Share a volume among several containers  

Why use a data container vs a created volume?  

------------------------------------------------------------------------------
