# Visitor IP

Simple application which shows IP of client who just made a request.

## Development

Environment for development can be established in two ways: Docker and local.
Follow below instructions for a method you'd like to apply.

### Docker

To use Docker for local environment you need to have Docker or Podman installed.
Just invoke `docker-compose up -d` command to run environment.
Application will be available at `http://localhost:5000` once ran correctly.

Please note, that `src` directory is mounted as a volume to the container.
Also, application is executed in _development_ mode, so it'll auto-reload
upon changes made to files.

### Local environment

If you wish to work on this app locally, you need to have installed:

- Python 3.11 (can be installed using `pyenv` if you don't have it)
- `pipenv`

```bash
# Prerequisites
pyenv install 3.11 # optional if you have correct version
pyenv shell 3.11   # in your system already
pip install pipenv

# Project setup
pipenv install
```

To run your project for development, just invoke

```bash
pipenv run flask --app src/app.py

# Alternatively
pipenv shell
pipenv run flask --app src/app.py
```

## Preparing production image

To create image with production version of the application, create Docker
image and tag it appropriately. Then you can push it to your container registry
and apply on a cluster using Kubernetes.

```bash
# Set your registry
export REGISTRY=my-registry:5000

# Preparing image
docker build -t visitorip:latest .

# Pushing image to registry
docker image tag visitorip:latest $REGISTRY/visitorip:latest
docker image push $REGISTRY/visitorip:latest
```

## Applying Kubernetes files

To deploy this application on cluster, add deployment and service to your
Kubernetes cluster. K8s files are placed under `k8s` directory

```bash
kubectl apply -f k8s/deployment-visitorip.yml
kubectl apply -f k8s/service-visitorip.yml
```

You can reach the service by retrieving Node IP and appropriate port. To do so,
invoke below commands and visit found IP and port using web browser or API
testing program, like Postman or Insomnia.

```bash
kubectl get node -o wide # Here you have INTERNAL-IP of your node
kubectl get services # Find your service and port after 80: for it
```
