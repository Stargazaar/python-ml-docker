# Docker ML Project
This project demonstrates a complete end-to-end machine learning workflow, containerized with Docker and orchestrated with Kubernetes. The primary objective is to learn and apply best practices for deploying a Python-based FastAPI machine learning application.
The application uses a simple Logistic Regression model trained on the Iris dataset to predict flower species. It includes a basic web frontend for user interaction and a fully automated CI/CD pipeline using GitHub Actions.
## Tech Stack
- **Backend**: FastAPI, Uvicorn
- **Machine Learning**: Scikit-learn, NumPy
- **Frontend**: HTML, JavaScript (no framework)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (via Docker Desktop)
- **CI/CD**: GitHub Actions
- **Testing**: Pytest, httpx

1. github initialize
create new repo from template
git clone git clone https://github.com/Stargazaar/python-ml-docker.git

cd to the repo
cd python-ml-docker                                          

Switch to feature branch (best practice)
git checkout -b feature/docker-k8s
git add .
git commit -m "Initial commit for branch"
git push --set-upstream origin feature/docker-k8s


2. Open Docker desktop but CMD In IDE: Build docker image. cd to folder containing Dockerfile.
docker build -t qk8128/ml-docker:latest .

3. Push the image to a container registry (like Docker Hub):
docker login
docker push qk8128/ml-docker:latest

4. Update deployment.yaml.
Replace your-docker-hub-username/ml-docker:latest with the actual path to your pushed image.

5. Deploy to Kubernetes:
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

6. Check status of Kubernetes deployment:
kubectl get deployment ml-docker-deployment
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
ml-docker-deployment   1/1     1            1           117s

7. Get service URL
Since we are using DockerDesktop, we use NodePort instead of LoadBalancer, hence no external IP
NAME                TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
ml-docker-service   NodePort   10.110.235.122   <none>        80:30420/TCP   11m

http://localhost:30420/static/index.html should work and show the app.

# When need to redeploy after making changes:
1. docker build and push:
a. docker build -t qk8128/ml-docker:latest .
b. docker push qk8128/ml-docker:latest
If github actions is enabled, it will do this automatically. upon merging to main branch.
git checkout main
git merge feature/docker-k8s
git push origin main
2. kubectl rollout restart deployment ml-docker-deployment

# For Github Actions CICD. 
1. Create .github/workflows/main.yml
2. If there are secrets needed, e.g. username: ${{ secrets.DOCKER_USERNAME }} and password: ${{ secrets.DOCKER_PASSWORD }}, add to github secrets as such: 
a. Go to your GitHub repository page.
b. Click on the Settings tab.
c. In the left sidebar, expand Secrets and variables, then click on Actions.
d. Click the New repository secret button.
e. Create a secret with the name DOCKER_USERNAME and your Docker Hub username 'qk8128' as the value.
f. Repeat for Docker_PASSWORD