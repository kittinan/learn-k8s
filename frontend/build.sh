#!/bin/bash
IMAGE_NAME="kittinan/learn-k8s"
IMAGE_TAG="frontend"
# Build the Docker image for the frontend
# and push it to the Docker registry

docker build -t $IMAGE_NAME:$IMAGE_TAG . && docker push $IMAGE_NAME:$IMAGE_TAG