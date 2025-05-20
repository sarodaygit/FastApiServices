#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Build the Docker image
docker build -t fastapiservices -f Deployment/Dockerfile .

# Run the Docker container in detached mode
docker run -d -p 8004:8004 fastapiservices

# List running Docker containers
docker ps

# Get the container ID of the running container
container_id=$(docker ps -q --filter ancestor=fastapiservices)

Execute a bash shell inside the running container
if [ -n "$container_id" ]; then
  echo "Dune FastApi Service Docker is running  with container ID :- "$container_id" "
else
  echo "No running container found for the image fastapiservices"
fi
