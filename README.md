# Counter Service

The Counter Service is a simple Flask application that increments a counter with each POST request and displays the counter value on GET requests. This application is containerized using Docker and deployed to an Amazon EKS cluster through automated CI/CD pipelines with GitHub Actions.

## Application Overview

The application provides a simple RESTful service that:
- **Increments** a counter with each POST request to the root (`/`).
- **Displays** the counter on GET requests to the root (`/`).

## Repository Structure

- **Dockerfile**: Contains the Docker configuration for building the application image.
- **app**:
  - `counter-service.py`: The Flask application script.
- **k8s**:
  - `deployment.yaml`: Kubernetes deployment configuration.
  - `services.yaml`: Kubernetes service configuration.
  - `namespaces.yaml`: Kubernetes namespace configuration.
- **.github/workflows**:
  - `docker-build-push.yml`: GitHub Actions workflow for building, pushing the Docker image, and deploying to Kubernetes.

