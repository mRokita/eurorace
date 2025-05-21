#!/bin/bash

# Stop any running containers
docker-compose down

# Build and run the test service
docker-compose build test
docker-compose run --rm test

# Clean up
docker-compose down