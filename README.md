## INSTALL DOCKER ON UBUNTU(if not exsit)
[中文版](https://yeasy.gitbook.io/docker_practice/install/ubuntu)
[English](https://docs.docker.com/engine/install/ubuntu/)

## DO IT MYSELF:pytorch_Ubuntu1604_docker

----------

`cat pytorch.Dockerfile >> .Dockerfile`

`docker build -t IMAGE_NAME[:TAG] -f Dockerfile .`
  

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
