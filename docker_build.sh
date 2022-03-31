#!/bin/sh

echo "Building Docker Image"
docker build -t selenium_in_docker_image .

#echo "Running Docker Container"
#docker run --name selenium_in_docker_container -v $(pwd):/home/user78/Desktop/docker-selenium/scripts/main.py selenium_in_docker_image