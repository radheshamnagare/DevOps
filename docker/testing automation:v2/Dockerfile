FROM ubuntu:20.04

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3 python3-distutils python3-pip python3-apt
RUN apt-get install -y git 
RUN apt-get install -y curl
RUN apt-get install -y jq

COPY requirements.txt  requirements.txt

RUN pip3 install -r requirements.txt

COPY create_git_access_token.sh create_git_access_token.sh

RUN  chmod +x create_git_access_token.sh 
RUN  chmod +x create_git_access_token.sh
CMD [ "./create_git_access_token.sh" ]
