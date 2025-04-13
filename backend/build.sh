#!/bin/bash
IMAGE_NAME="kittinan/learn-k8s"
IMAGE_TAG="backend"
# Build the Docker image for the backend
# and push it to the Docker registry

docker build -t $IMAGE_NAME:$IMAGE_TAG . && docker push $IMAGE_NAME:$IMAGE_TAG