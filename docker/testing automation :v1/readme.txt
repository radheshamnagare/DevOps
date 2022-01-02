
run following commands in docker

1-upzip auto_testing.zip

2-then go to that dir on the terminal

 if u wish push image in docker hub then put docker username like username/auto_testing:latest
3-sudo docker build -t auto_testing:latest

list the images
4- sudo docker images

5- find image auto_testing:latest

6-copy images id of auto_testing:latest

ur script will automaticaly run 
7-sudo docker run -it image_id





