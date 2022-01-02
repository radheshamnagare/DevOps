#DevOps

# Docker 
  Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channel.
  
  ### Docker installation
     follow the docker installation on https://github.com/radheshamnagare/Docker-Installation
 - ## Fast-Api
  `
    We used fastapi in finmarka project for that we need virtualization to deliver software we also database persistant layer .
    for that all specific need grab together we used docker.`
 
 ### How to run
  1. Either fork or download
  2. Open in cli
  3. Build the docker image
  ```
  docker build -t fastapi:latest .
  ```
  4. After build the image we will find it
   ```
   docker images fastapi:latest
   ```
  5. Run the fastapi
  ```
   docker run -p 80:9000 fastapi:latest
   ```
    it will serve http://localhost/
   
  6. You can see in the browser just hit `localhost/`
     

- ## Testing-automation
   we need to testing the code work through testing api .afer run the api it will download all remote github repository and test and show the testing resultl.
   
   ### How to run
   
   1.  Open in the cli
   2.  Build the docker image 
     ```
     docker build -t testautomation:latest .
     ```
   3.  Find the image
    ```
    docker images testautomation:latest
    ```
   4.  Run the docker image
    ```
    docker run testautomation:latest
    ```
   
   
 # Kubernates 
 Kubernetes is an open-source container-orchestration system for automating computer application deployment, scaling, and management.
 It was originally designed by Google and is now maintained by the Cloud Native Computing Foundation.
 
 ## Installation
   Follow the kubernates installation on https://github.com/radheshamnagare/Kubernates-Installation
   
 ##  How it work
   All are `.yml` confriguration files just we need to apply it
   
   1. How to apply confrigution in kubernates
   ```
      kubectl apply `file_name.yml`
   ``` 
   2. It will find
   ```
      kubectl get pods
   ```
     
   4. Run th pod
   ```
     kubctl run pod pod_name
   ```
     
   5. we can inspect it also
   
   ```
   kubectl inspect pod_name
   ```
   
   
   
   
 # Ingress-operator
 The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based Ingress Controllers to handle routing. You can use the Ingress Operator to route traffic by specifying OKD Route and Kubernetes Ingress resources. Configurations within the Ingress Controller, such as the ability to define endpointPublishingStrategy type and internal load balancing, provide ways to publish Ingress Controller endpoints.
 
 In this ingress operator directory we will find how we can confrigure our services through ingress-operator
 
 ## Reference
  - https://docs.okd.io/latest/networking/ingress-operator.html
  - https://www.openfaas.com/blog/custom-domains-function-ingress/
  
   
 # Open-faas
 OpenFaaS is an open-source framework for implementing the serverless architecture on Kubernetes, using Docker containers for storing and running functions. It allows any program to be packaged as a container and managed as a function via the command line or the integrated web UI
 
 ## Installation & workshop
  follow on https://github.com/radheshamnagare/Openfaas-Workshop
  
## How to run
1. we need docker ,kubernates installed on the machine
2. After that we need openfass cli `faas-cli`
3. Open the reposotory in cli
4. Build the function
```
faas-cli build -f filename.yml --prefix dockerhub_username
```
5. Push the function
```
faas-cli push -f filename.yml
```
6. Deploy the function
```
faas-cli depoy -f filename.yml
```

   
 # Test Fastapi
This is bit more advance ,here we used docker-compose

## How to run
1. Build image

```bash 
sudo docker-compose build
```
2. start the service
```bash 
sudo docker-compose up
```
3. it will serve http://localhost:9000



# All Reference
- https://www.openfaas.com/
- https://kubernetes.io/
- https://www.katacoda.com/
- https://kodekloud.com/

