# Docker + Flask Tutorial

*Tutorial by: Madalyn Marabella*

This tutorial will show you how to create a simple flask app using Docker. Docker is a tool for creating and coordinating containers.

### Part 0: Vocabulary
* **Image**: text
* **Container**: text
* **Dockerfile**: text

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

1. Get files from the flask-docker-simple folder. For this section of the tutorial, you do not need the files in flask-docker-postgres folder, so you can either
A. clone the whole repository and navigate inside the flask-docker-simple directory
B. just download/copy the files from flask-docker-simple
2. Run the 'docker build' command below.
```
$ docker build -t flask-simple:0.1 .
```
3. Execute the 'docker run' command below. 
```
$ docker run -p 5000:5000 flask-simple:0.1
```

**Explanation of `docker build` and `docker run`:**
'Docker build' uses the dockerfile to create a docker **image**, which is a template for building docker **containers**. Using the specifications in the docker image, 'docker run' creates a docker **container** (an isolated environment) and runs a series of instructions inside. One of the specifications in the dockerfile is `RUN pip install -r requirements.txt`, so the container built by 'docker run' will have Flask installed. Then docker runs the command specified in the dockerfile. Our dockerfile has an `ENTRYPOINT` of "python" and the `COMMAND` "app.py", so it will run `python app.py` inside the container, which starts the Flask server.
