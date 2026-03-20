#  Theory – Containerization and DevOps

This folder contains **class-wise theory notes** for the subject  
**Containerization and DevOps**.

The notes include both **conceptual understanding** and **command-level explanations** wherever required.

---

##  Class-wise Notes

###  Class 1 – Docker Basics (Hands-on)
Topics covered:
- Docker introduction
- Docker architecture overview
- Basic Docker commands
- Image and container lifecycle

 [Open Class 1 Notes](Class1/README.md)

 ###  Class 2 – Preserving Changes in Containers
Topics covered:
- Running Ubuntu container
- Installing software inside container (OpenJDK 17)
- Creating and running a Java application
- Understanding container filesystem changes
- Preserving changes using docker commit
- Creating and running a custom Docker image

 [Open Class 2 Notes](Class2/README.md)

### Class 3 – Dockerfile Automation (Java App)
Topics covered:
- Dockerfile basics
- Building custom images with automation

 [Open Class 3 Notes](Class3/README.md)

### Class 4 – Docker Engine API with curl
Topics covered:
- Interacting with Docker daemon via Unix socket
- Container lifecycle control using curl (create, start, rename, commit)

 [Open Class 4 Notes](Class4/README.md)

### Class 5 – Multi-Stage Builds in Docker
Topics covered:
- Single-stage vs Multi-stage Dockerfiles
- Compiling a C application
- Image size optimization

 [Open Class 5 Notes](Class5/README.md)

### Class 6 – Docker Volumes and Bind Mounts
Topics covered:
- Persistent storage in Docker
- Managing Docker Volumes (`docker volume create/inspect`)
- Attaching Volumes using `-v` and `--mount` syntax
- Bind mounts to host directories

 [Open Class 6 Notes](Class6/README.md)

### Class 7 – Docker Networks
Topics covered:
- Docker Networking Concepts
- Default Bridge Network vs Custom Bridge Networks
- Inter-container communication
- Host Network configuration

 [Open Class 7 Notes](Class7/README.md)

### Class 8 – Docker Compose Basics
Topics covered:
- Declarative multi-container orchestration with `docker-compose.yml`
- Basic Nginx container setup using Compose
- Multi-container application setup (WordPress & MySQL)
- Compose lifecycle commands (`up`, `down`, `logs`, `ps`)

 [Open Class 8 Notes](Class8/README.md)

### Class 9 – Docker Compose Web Apps (NGINX Proxy)
Topics covered:
- Scaling containers with Docker Compose
- Resolving port conflicts using port ranges
- Setting up an NGINX reverse-proxy load balancer
- Routing traffic over internal Docker networks

 [Open Class 9 Notes](Class9/README.md)

### Class 10 – Docker Swarm Basics
Topics covered:
- Initializing a Docker Swarm cluster
- Creating and inspecting replicated services
- Scaling services up and down
- Publishing ports in Swarm mode
- Managing Swarm service lifecycle

 [Open Class 10 Notes](Class10/README.md)

### Class Task – Python SAP ID Application Containerization
Topics covered:
- Containerizing a Python interactive script
- Verifying terminal prompts using `docker run -it`
- Managing basic Python dependencies

 [Open Class Task Notes](ClassTask/README.md)
