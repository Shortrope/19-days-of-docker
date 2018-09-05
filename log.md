
<!-- 
## Day N: August N, 2018 - Nhr
**Today's Progress**:  
**Thoughts:**  
**Link to work:**  
<br><br>

---
-->

# 19 Days Of Docker - Log

## Day 24: August 5, 2018 - 1hr
**Today's Progress**:  
Finish Chap 9: Stacks  
Deploy services with stacks.  Similar to docker-compose  

**Thoughts:**  
This is what I was looking for to deploy my Wordprss services

**Link to work:**  
[Chap 9 Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Getting%20Started%20w%20Docker%20Swarm%20Mode/9%20Deploying%20w%20Stacks.md)
<br><br>

---
## Day 23: August 4, 2018 - 1hr
**Today's Progress**:  
Finish Chap 8: Networking

**Thoughts:**  

**Link to work:**  
[Chap 8 Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Getting%20Started%20w%20Docker%20Swarm%20Mode/8%20Networking.md)
<br><br>

---
## Day 22: August 3, 2018 - 3.5hr
**Today's Progress**:  
Mess with volumes on mysql and wordpress   
Backup, destroy and restore a Wordpress setup  
- backed up the volumes w rsync to a local dir on the host
- Dstroy the containers and volumes (docker-compose down)
- `docker-compose up` (for a fresh install)
- `docker-compose stop` 
- rsync'ed the files back to the new volumes
- `docker-compose start` 
- Restored! It all worked.

**Thoughts:**  
Need to come up with better method for backup/restore.
Next try this with docker swarm  


**Link to work:**  
[Volume with MySQL](https://github.com/Shortrope/19-days-of-docker/blob/master/Projects/mysql/Dockerfile)  
[Volumes on WP and MySQL for backup/restore](https://github.com/Shortrope/19-days-of-docker/blob/master/Projects/wordpress/wpv2/docker-compose.yml)
<br><br>

---
## Day 21: August 2, 2018 - 3hr
**Today's Progress**:  
Finish Chap 5  Ingress Routing and publishing ports  
Finish Chap 6  Reconciling Desired State  
Finish Chap 7  Rolling updates  

**Thoughts:**  
Internal routing and load balancing.. awesome!  
Rolling update are cool.. but the chap was too long

**Link to work:**  
- [Chap 5 Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Getting%20Started%20w%20Docker%20Swarm%20Mode/4%20Ingress%20Routing%20and%20Publishig%20Ports.md)  
- [Chap 6 Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Getting%20Started%20w%20Docker%20Swarm%20Mode/6%20Reconciling%20Desired%20State.md)  
- [Chap 7 Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Getting%20Started%20w%20Docker%20Swarm%20Mode/7%20Rolling%20Updates.md)
<br><br>

---
## Day 20: September 1, 2018 -2hr
**Today's Progress**:  
Finish Chap 4 'Adding Nodes'  
Add nodes. Scale up a service across nodes
Drain nodes

**Thoughts:**  
Still super cool!  Adding/Scalling up a service across nodes is super easy.  

**Link to work:**  
[Adding Nodes notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Getting%20Started%20w%20Docker%20Swarm%20Mode/3%20Adding%20Nodes.Notes.md)
<br><br>

---
## Day 19: August 31, 2018 - 1.5hr
**Today's Progress**:  
Finish Chap 3 'Getting Started w Docker Swarm Mode'  
Spin up an Nginx service.. then scale the instances up and down  

**Thoughts:**  
Super cool stuff!!!  

**Link to work:**  
[Notes](https://github.com/Shortrope/19-days-of-docker/tree/master/Getting%20Started%20w%20Docker%20Swarm%20Mode)
<br><br>

---
## Day 18: August 30, 2018 - 2.25hr
**Today's Progress**:  
Created an apache2, httpd and mysql containers individually.  Had tough time connecting to the 
mysql container (changed from v8.0 to 5.7 then worked).  
Created mysql and a Wordpress container manually and got Wordpress working  
Created a docker-compose.yml file to spin up the Wordpress/mysql services.

**Thoughts:**  
This was my real goal to spin up a wordpress instance with docker.  
But I am now interested in swarm and will continue on.

**Link to work:**  
1. [apache2 and httpd](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/apache)
1. [Wordpress](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/wordpress)
<br><br>

---
## Day 17: August 29, 2018 - 1.5hr
**Today's Progress**:  
Reviewing vids.  trouble w docker-compose.. errors. needed to update to latest version.  
Worked with ARG in Dockerfile  

**Thoughts:**  
Difficult trying anything new. I was into it today but still feels like super slow progress.  

**Link to work:**  
[Project/args](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/args)
<br><br>

---
## Day 16: August 28, 2018 - 1hr
**Today's Progress**:  
Signed up on Pluralsight to learn about Swarm and maybe Kubernetes
Start a couple of courses.. settled on Getting Started w Docker Swarm Mode

**Thoughts:**  
Swarm looks awesome!!

**Link to work:**  
[Managing Docker Swarm .. But then I started a different course](https://github.com/Shortrope/19-days-of-docker/tree/master/Managing%20Docker%20Swarm)
<br><br>

---
## Day 15: August 27, 2018 - 1hr
**Today's Progress**:  
Created an Apache image with a Dockerfile.  
Used RUN, COPY, VOLUME, EXPOSE, ENTRYPOINT, CMD  
Copied html and css files into the container  
Edited the html and css in the volume while the container was running  
Exported and imported the container to another machine.  

**Thoughts:**  
Now starting to get more practical.  
Very interested in swarm

**Link to work:**  
[Apache project](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/apache)
<br><br>

---
## Day 14: August 26, 2018 - 2.5hr
**Today's Progress**:  
Finished last two sections of the video course: Volumes, Networking, TShooting

**Thoughts:**  
Better understanding of Dockerfiles and networking. Definitly worth going thru.

**Link to work:**  
[Update chap 6 notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Chap6.RunningServicesInContainers.md)
<br><br>

---
## Day 13: August 25, 2018 - 3.5hr
**Today's Progress**:  
Docker Vids: Mainly a review but picking up some points not taught in the book.
- Image layers
- Image `save` and `load` (export/import)  
- Pid 1 process running in a container
- Dockerfile commands: RUN, CMD, ENTRYPOINT, ENV

Started a command reference file

**Thoughts:**  

**Link to work:**  
[Command Reference](https://github.com/Shortrope/19-days-of-docker/blob/master/CommandReference.md)
<br><br>

---
## Day 12: August 24, 2018 - 0hr
Skipped.. went to Borrego Springs.  
Spent maybe 20mins reading the Docker website
<br><br>

---
## Day 11: August 23, 2018 - 1.5hr
**Today's Progress**:  
Started reading the Docker web site docs since I have been stuck.
Did an example with docker swarm (new) and docker-compose

**Thoughts:**  
The example done today was very cool spinning up 5 containers. Some excitement back, but it 
introduced new commands I have not seen yet.  Will have to reveiw again.

**Link to work:**  
1. [python container example](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/get-started-p2-python)
1. [docker swarm example](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/get-started-p3-compose1)
<br><br>

---
## Day 10: August 22, 2018 - 1.25hr
**Today's Progress**:  
Try to create simple Dockerfile to update the hosts and hostname files with a RUN command
Failed, did not work

**Thoughts:**  
Can't seem to get the simplest thing to work. Frustrating

**Link to work:**  
[Dockerfile](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/apache)
<br><br>

---
## Day 9: August 21, 2018 - 1hr
**Today's Progress**:  
Strange day. Tough to make any progress. Trying to launch using docker compose. Not doing what I 
want it to.

**Thoughts:**  
Feeling a bit lost trying to put it all together. Felt like virtually no progress today.

**Link to work:**  
[docker-compose.1.yml](https://github.com/Shortrope/19-days-of-docker/blob/master/Projects/MySQL.svrclient/docker-compose.1.yml)  
Does not work ^
<br><br>

---
## Day 8: August 20, 2018 - 1hr
**Today's Progress**:  
Work on MySQL Svr Client: mess with volumes to persist data.
Start looking at docker-compose.yml to launch with volumes

**Thoughts:**  
Difficult hour. Difficult to make any progress.

**Link to work:**  
[MySQL Svr Client](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/MySQL.svrclient)
<br><br>

---
## Day 7: August 19, 2018 - 2.5hr
**Today's Progress**:  
Chap 8: Orchestrating Containers
Test the in-built DNS
Create and run the Node-Redis docker-compose example

**Thoughts:**  
The Docker microservices architecture is starting to make some sense
The docker-compose example is very cool!!.  Kept my attention for an hour straight.. very focused!

**Link to work:**  
1. [Chap 8 Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/Chap8.OrchestratingContainers.md)
1. [Node Redis project](https://github.com/Shortrope/19-days-of-docker/tree/master/Chap8/nodeRedis)
<br><br>

---
## Day 6: August 18, 2018 - 1hr
**Today's Progress**:  
Finish Chap 7. Sharing data  
Break notes into separate files for each chapter  
Start compiling list of things to review and test myself on  

**Thoughts:**  
Still missing something.. not sure the practicality yet. 

**Link to work:**  
[Apache Log Reader Scenario](https://github.com/Shortrope/19-days-of-docker/commit/1f1f89ebb37268bcf53601a53ed669dea234dc1f)
<br> <br>

---

## Day 5: August 17, 2018 - 1.5hr
**Today's Progress**:  
Sharing/mounting a local directory or file in a container  
Sharing/mounting a containers data volume in other containers

**Thoughts:**  
Some how this seems like management can get out of hand quickly. Curious to find out how all this plays
out in a practical scenario

**Link to work:**  
[Updated Notes](https://github.com/Shortrope/19-days-of-docker/commit/2ac47774eea85c75731cc51520f6ddf13f6932dc)
<br> <br>

---
## Day 4: August 16, 2018 - 1hr
**Today's Progress**:  
Reviewed network bridge and host types  
Continued with Volumes

**Thoughts:**  
The book is very shallow on networking. Will have to find another source to dive deeper into this
subject.

**Link to work:**  
[Updated Notes](https://github.com/Shortrope/19-days-of-docker/commit/3fdb2f9d226b35ec1b0b7ccac91dcf3385c1fd75)
<br> <br>


---
## Day 3: August 15, 2018 - 1hr
**Today's Progress:**  
Create and connect to a MySQL container  
Trouble connecting until I inspected the container and realized it is on the 'bridge' network by
default.  Its IP was 172.17.0.2!.  Installed the mysql client on the host and was able to connect.  

**Thoughts:**  
Today wanted to do a practical project.  

**Link to work:**  
[MySQL Docker file and Notes on connecting to the container](https://github.com/Shortrope/19-days-of-docker/tree/master/Projects/mysql)
<br> <br>


---
## Day 2: August 14, 2018 - 1hr
**Today's Progress**:  
First section of chap 7 Volumes  
Could see where persistant volumes are stored and that they are not deleted automaticaly with the
container... This means they could be orphaned (like temp files growing)

**Thoughts:**  
Little tougher to start today. Tired from busy work day, but first pomodoro went by quickly.

**Link to work:** 
1. [Notes.md](https://github.com/Shortrope/19-days-of-docker/blob/master/LearningDocker.NOTES.md)
1. [git diff of notes](https://github.com/Shortrope/19-days-of-docker/commit/eab13101b50cf83f2509b1dca621cc42897a29fd)
<br> <br>


---
## Day 1: August 13, 2018 - 2hr

**Today's Progress**:  
Finished Chap 6: Binding ports and IP addresses  
Start Chap 7: Volumes

**Thoughts:**  
Things are coming to gether now that I can connect to a service in a container

**Link to work:** 
1. [My Docker Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/LearningDocker.NOTES.md)
2. [MountPointDemo Dockerfile](https://github.com/Shortrope/19-days-of-docker/tree/master/Chap7/volumes)

