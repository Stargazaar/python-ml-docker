# Docker ML Project

1. github initialize
create new repo from template
git clone git clone https://github.com/Stargazaar/python-ml-docker.git

cd to the repo
cd python-ml-docker                                          

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

http://localhost:30420 should work and show the app.