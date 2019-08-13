#based on the image from nvidia on dockerhub which includes ubuntu16.04,cuda9.0 and cudnn7
FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# Set the working directory to /home ,the command can be put anywhere in the dockerfile,which determines your initial dir
WORKDIR /home

# Copy the current directory contents into the container at /home
COPY . /home
# Copy the source.list in the upper directory  to the container at /etc/apt/
#the source.list include the url of tsinghua mirrors which will help the download of ubuntu
COPY ../source.list /etc/apt/

RUN apt-get update && \
    apt-get install -y --fix-missing build-essential \
        wget \
        curl \
        git \
        openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    /bin/bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh 

#add '/opt/conda/bin/' to the front of past ENVPATH,and then the docker will find the pip in conda instead of the pip in the system default python path
ENV PATH=/opt/conda/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

#we don't use conda init/activate/install... because the path about conda command haven't been put into envpath
#pip install is the same as conda install,the below package will be installed at base environment of conda
#if you need tensorflow just pip in same command,there will be no conflict. 

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple torch torchvision

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple cython 

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy opencv-python matplotlib  


# Run nn_demo.py when the container launches at WORKDIR
CMD ["python", "nn_demo.py"]

