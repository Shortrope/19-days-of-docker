
<!-- 
## Day N: August N, 2018 - Nhr
**Today's Progress**:  
**Thoughts:**  
**Link to work:**  


---
-->

# 19 Days Of Docker - Log

## Day 5: August 17, 2018 - 1.5hr
**Today's Progress**:  
Sharing/mounting a local directory or file in a container  
Sharing/mounting a containers data volume in other containers

**Thoughts:**  
Some how this seems like management can get out of hand quickly. Curious to find out how all this plays
out in a practical scenario

**Link to work:**  
[Updated Notes](https://github.com/Shortrope/19-days-of-docker/commit/2ac47774eea85c75731cc51520f6ddf13f6932dc)


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
## Day 1: August 13, 2018 - 2hr

**Today's Progress**:  
Finished Chap 6: Binding ports and IP addresses  
Start Chap 7: Volumes

**Thoughts:**  
Things are coming to gether now that I can connect to a service in a container

**Link to work:** 
1. [My Docker Notes](https://github.com/Shortrope/19-days-of-docker/blob/master/LearningDocker.NOTES.md)
2. [MountPointDemo Dockerfile](https://github.com/Shortrope/19-days-of-docker/tree/master/Chap7/volumes)

