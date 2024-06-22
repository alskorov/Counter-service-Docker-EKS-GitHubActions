## CI/CD Pipeline

The CI/CD pipeline for the Counter Service is managed using GitHub Actions, which automates the processes of building the Docker image, pushing it to AWS Elastic Container Registry (ECR), and deploying the application to an Amazon EKS cluster.

### Workflow Breakdown

The `.github/workflows/docker-build-push.yml` file contains the GitHub Actions workflow that triggers on every push to the `main` branch. Here's what each step does:

1. **Checkout Code**
   - **Action Used**: `actions/checkout@v2`
   - **Purpose**: Checks out your repository under `$GITHUB_WORKSPACE`, so your workflow can access it.

2. **Login to Amazon ECR**
   - **Action Used**: `aws-actions/amazon-ecr-login@v1`
   - **Purpose**: Logs in to Amazon ECR with the AWS credentials provided to allow Docker images to be pushed to your AWS container registry.

3. **Build, Tag, and Push Image to Amazon ECR**
   - **Environment Variables**: Uses the output from the ECR login step to push the image.
   - **Commands**:
     ```bash
     docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
     docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
     ```
   - **Purpose**: Builds the Docker image from your Dockerfile, tags it appropriately, and pushes it to the specified ECR repository.

4. **Configure kubectl**
   - **Action Used**: `actions-hub/kubectl@v1`
   - **With Parameters**:
     - `version: '1.30.0'`
   - **Purpose**: Installs kubectl command-line tool on the runner for interacting with Kubernetes.

5. **Setup AWS CLI**
   - **Commands**:
     ```bash
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     unzip awscliv2.zip
     sudo ./aws/install
     ```
   - **Purpose**: Installs the latest version of AWS CLI to configure access to AWS services.

6. **Configure AWS credentials**
   - **Commands**:
     ```bash
     aws eks --region <region> update-kubeconfig --name <eks-cluster-name>
     ```
   - **Purpose**: Configures `kubectl` to interact with your Amazon EKS cluster by updating the kubeconfig file with the cluster details.

7. **Validate Kubernetes YAML files**
   - **Commands**:
     ```bash
     kubectl apply --dry-run=client -f k8s/namespace.yaml
     kubectl apply --dry-run=client -f k8s/deployment.yaml
     kubectl apply --dry-run=client -f k8s/service.yaml
     ```
   - **Purpose**: Validates the Kubernetes configuration files to ensure they are correctly formatted and all necessary resources are defined.

8. **Deploy to Kubernetes**
   - **Commands**:
     ```bash
     kubectl apply -f k8s/namespace.yaml
     kubectl apply -f k8s/deployment.yaml
     kubectl apply -f k8s/service.yaml
     ```
   - **Purpose**: Applies the Kubernetes configuration files to the cluster, creating or updating the namespace, deployment, and service as specified.

This CI/CD pipeline ensures that any updates to the application are automatically built, deployed, and managed efficiently, minimizing downtime and human error.
