PROJECT_NAME=lidm-app-milestone-backend
IMAGE ?= $(PROJECT_NAME)
TAG ?= local

-include .env
export

build:
	docker build -t ${IMAGE}:${TAG} -f docker/Dockerfile .

build-remote:
	docker build -t localhost:32000/${IMAGE}:${TAG} -f docker/Dockerfile .

push-remote:
	docker push localhost:32000/${IMAGE}:${TAG}

local:
	docker-compose -f docker/docker-compose.yaml -p ${PROJECT_NAME} up -d --build

k8s-configmap:
	kubectl create configmap ${PROJECT_NAME}-config --from-env-file=.env -n works01

k8s-apply: build
	-kubectl create namespace works01
	kubectl apply -n works01 -f k8s/
