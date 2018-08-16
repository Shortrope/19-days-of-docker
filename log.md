# 100 Days Of Code - Log

## Day 1: August 13, 2018 - 2hr

**Today's Progress**:  
Finished Chap 6: Binding ports and IP addresses
Start Chap 7: Volumes

**Thoughts:**  
Things are coming to gether now that I can connect to a service in a container

**Link to work:** 
1. [My Docker Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/LearningDocker.NOTES.md)
2. [MountPointDemo Dockerfile](https://github.com/Shortrope/19-days-of-docker/tree/master/Chap7/volumes)


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

---

<!-- 
## Day N: August N, 2018 - Nhr
**Today's Progress**:  
**Thoughts:**  
**Link to work:** 
-->
