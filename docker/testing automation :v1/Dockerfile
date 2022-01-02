FROM ubuntu:20.04

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.8 python3-distutils python3-pip python3-apt
RUN apt-get install -y git 

COPY requirements.txt  requirements.txt

RUN pip3 install -r requirements.txt

COPY testframe.py testframe.py
COPY gitfile.sh gitfile.sh
COPY mypython.sh mypython.sh

RUN  chmod +x gitfile.sh 
RUN  chmod +x mypython.sh
CMD [ "./gitfile.sh" ]

