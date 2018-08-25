
<!-- 
## Day N: August N, 2018 - Nhr
**Today's Progress**:  
**Thoughts:**  
**Link to work:**  
<br><br>

---
-->

# 19 Days Of Docker - Log

## Day 13: August 25, 2018 - 2hr
**Today's Progress**:  
Docker Vids: Mainly a review but picking up some points not taught in the book.
- Image layers
- Image `save` and `load` (export/import)  
- Pid 1 process running in a container
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

