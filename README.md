## INSTALL DOCKER ON UBUNTU(if not exsit)
[中文版](https://yeasy.gitbook.io/docker_practice/install/ubuntu)
[English](https://docs.docker.com/engine/install/ubuntu/)
      
      docker version

## DO IT MYSELF:pytorch_Ubuntu1604_docker

`cat pytorch.Dockerfile >> .Dockerfile`

`docker build -t IMAGE_NAME[:TAG] -f Dockerfile .`

----------
  

the docker is based on the image from nvidia on dockerhub which includes ubuntu16.04,cuda9.0 and cudnn7.
### Contains
+ wget
+ curl
+ git 
+ openssh-server  
+ miniconda \[base\] pytorch numpy matplotlib opencv-python cython

other supplementary information

- code annotation
- example of docker common commands

## AVOID REINVENTING THE WHEEL:dockerhub

`docker pull iyzf/pytorch:cuda`

* ubuntu 16.04
* cuda 9.0
* python 3.7
* pytorch 1.1

`docker pull hexiffer/pytorch:stable`

the stable version made by a Ph.D student in my lab

## SOMETHING ELSE

[offical tutorial](https://docs.docker.com/get-started/)
key points :

* Image 
* Container 
* Repository 

### An example:run keras in docker
      docker pull floydhub/tensorflow:1.11-py3_aws.40 
      sudo docker run --name mykerasimg -p 6006:6006 -p 8888:8888  floydhub/tensorflow:1.11-py3_aws.40 # expose jupyter+tensorboard's port
      sudo docker stop mykerasimg 

the next time to run the image

    sudo docker start mykerasimg # run jupyter automatically 
    sudo docker exec -it mykerasimg bash #run a container with tty and interact
    root@31c952a2e3ea:/# jupyter notebook list

\>\>\> Currently running servers: 
http://localhost:8888/?token=balbalbalba  

    sudo docker stop mykerasimg
    
if you no longer use the image

     sudo docker container ls
     sudo docker rm  $container_ID$
     sudo docker ps -a 
     sudo docker image ls
     docker image rm $image_name$
