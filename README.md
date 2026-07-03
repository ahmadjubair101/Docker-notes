# Docker Learning

This repository showcases my learnings and findings of Docker, from note taking and important concepts to building and creating projects which include: understanding and running containers, managing multi-container applications with the usage of Docker Compose and utilising public and private registry's through Docker Hub and AWS ECR to push images. Applying these concepts into practical application has helped solidy my understanding of how this contributes to DevOps as a whole.

# Concepts and key information I have learnt
- **What is Docker:** Understanding containers, their utility, comparisons to virtual machines, and why Docker is crucial in modern DevOps.

- **Key Container Concepts:** Building images with (docker build), running containers using (docker run), inspecting them through (docker inspect), and managing them such as stopping and removing them through (docker stop, docker rm).

- **Importance of Networking and Volumes:** Connecting containers to a network in order for services to communicate and utilising volumes to persist data further and beyond containers.

- **Docker Hub & AWS ECR (Public and Private registry's):** Becoming familiar with public (Docker Hub) and private registries (AWS ECR), implementing pushing and pulling through both registries whilst also practicing authentication and tagging workflows.

- **Docker Compose (Multi-Container Applications):** Comparing manual docker container creation to Docker compose, creating multi-container applications with the usage of docker-compose.yml file, defining services, pointing towards ports, and changing networks and dependencies.

- **Multi-stage builds for Docker Images:** Using multi-stage builds to reduce overall resource size on an image, removing unnecessary dependencies, leading to more storage conserving, efficient production-ready containers.

- **Logs & Debugging Docker:** Inspecting containers and images, reviewing logs and troubleshooting issues between containers to direct to a solution such as networking.

- **Cleanup of Docker environment:** Ensuring a clean Docker environment by removing unused images and containers by stopping running containers or removing them completely through commands such as docker system prune.

- **Container Orchestration Brief Introduction:** Introduction to Kubernetes and Docker Swarm and why container orchestration is important for: scaling and managing containers across multiple machines ensuring they run smoothly.

# Docker Project: Flask + Python+ MySQL application

This is showcased on the hello_flask folder within this repo.

# Docker Challenge: Flask + Redis Multi-Container (Docker Compose) Application

To put these concepts into practice, I built a multi-container application which consisted of:

- A Python- Flask web application that showcases a welcome page and a count on how many visits the page gets.
- A Redis database to store these counts utilising persistent storage.

Key concepts and tools applied in this challenge:

- **Dockerfile**- Used to place the Flask application in a container.
- A **Redis** Docker image to connect to Flask.
- These services are managed and run through **Docker Compose**, ensuring the correct networking attributes and dependencies.
- Utilising **persistent storage** with Docker volumes, so Redis data retains when containers are restarted.
- Experimentation with **environment variables** and **scaling services** (bonus challenge).

By completing this challenge, I was able to understand how Docker allows consistent application deployment across environments and how containerisation simplifies development, testing and production workflows.
