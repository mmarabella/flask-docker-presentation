# Docker + Flask Tutorial

*Tutorial by: Madalyn Marabella*

This tutorial will show you how to create a simple flask app using Docker. Docker allows developers to create and deploy apps is isolated, easy-to-manage runtime environments. Dockerfiles and yaml files define all the packages, libraries, variables, etc. to run a code and all its dependencies in self-contained packages. With Docker, developers do not have to worry about differences in operating systems and installed software.

### Part 0: Vocabulary
* **Image**: executable that defines all the libraries, variables, and configurations needed to run a part of an application; i.e. a template for building a container
* **Container**: isolated package running in memory, containing code and all its dependencies; i.e. an instance of an image
* **Dockerfile**: list of instructions that run to set up a container; much of the information contained in a dockerfile can also be defined by docker-compose.yml
* **Service**: part of an application, for example a database or a server; one or multiple identical containers will carry out a service
* **Docker Compose**: tool for setting up a docker app with multiple containers; uses a yaml file to define an app's services and the relationships between those servies

### Part 1: Install Docker
```
$ docker run hello-world
```
You should receive the message:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### Part 2: Build and run image

**For this section of the tutorial, reference the files in the flask-docker-simple folder.** The flask-docker-simple folder contains everything you need to build a simple docker app!

1. Get files from the flask-docker-simple folder. For this section of the tutorial, you do not need the files in flask-docker-postgres folder.
A. clone the WHOLE repository (flask-docker-app)
B. navigate inside the flask-docker-simple folder
2. Run the 'docker build' command below.
```
$ docker build -t flask-simple:0.1 .
```
3. Execute the 'docker run' command below. 
```
$ docker run -p 5000:5000 flask-simple:0.1
```
4. Go to localhost:5000. Your app should be running!

**Explanation of Part 2**
'Docker build' uses the dockerfile to create a docker **image**, which is a template for building docker **containers**. Using the specifications in the docker image, 'docker run' creates a docker **container** (an isolated environment) and runs a series of instructions inside. One of the specifications in the dockerfile is `RUN pip install -r requirements.txt`, so the container built by 'docker run' will have Flask installed. Then docker runs the command specified in the dockerfile. Our dockerfile has an `ENTRYPOINT` of "python" and the `COMMAND` "app.py", so it will run `python app.py` inside the container, which starts the Flask server.


### Part 3: 'Docker compose' & connecting to a database

**For this section of the tutorial, reference the files in the flask-docker-postgres folder.** You no longer need the files in flask-docker-simple.

1. Navigate inside the flask-docker-postgres folder
2. Run `docker-compose up`
3. Go to localhost:5000. Your app should be running!

**Explanation of Part 3**


Take a look at the files inside the flask-docker-postgres folder.
