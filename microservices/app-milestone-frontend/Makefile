PROJECT_NAME=lidm-app-milestone-frontend
IMAGE ?= $(PROJECT_NAME)
TAG ?= 1.0.5

-include .env
export

build-public:
	docker build -t ${IMAGE}-public:public -f docker/Dockerfile.public .

build-remote:
	docker build -t localhost:32000/${IMAGE}:${TAG} -f docker/Dockerfile.remote .

push-remote:
	docker push localhost:32000/${IMAGE}:${TAG}

k8s-configmap:
	kubectl create configmap ${PROJECT_NAME}-config --from-env-file=.env -n works01

k8s-apply: build
	-kubectl create namespace works01
	kubectl apply -n works01 -f k8s/
