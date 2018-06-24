# Example Dockerfile to demonstrate containerising an app
# Author: Robert Brown, South Bank University
# Date: 24/06/2018

# Instructions to build image: docker image build -t <name>:<version> .
# Example command (remember the dot): docker image build -t test:v1 .

# Instructions to run app as container and delete after running:
# docker container run --rm <name>:<version>
# Example command: docker container run --rm test:v1

# Instructions to run container and enter shell without running app:
# docker container run -it --rm test:v1 /bin/bash

# Choose an image to base the container on. This will be pulled from dockerhub.
FROM ubuntu:latest

# Run shell commands in image to install dependencies inside using package manager
RUN apt-get update && apt-get install -y python3

# Make a new directory inside image and set as current working directory
WORKDIR /app

# Copy all files from context folder on host to /app folder in image
COPY . /app

# Set command to be run when a container is run from the image, followed by it's arguments
CMD [ "python3", "app.py" ]

