PROJECT_NAME=lidm-app-milestone-gateway
IMAGE ?= $(PROJECT_NAME)
TAG ?= 1.0.2
NEW_RELIC_LICENSE_KEY ?= $(NEW_RELIC_LICENSE_KEY)

-include .env
export


build-remote:
	docker build -t localhost:32000/${IMAGE}:${TAG} -f docker/Dockerfile --build-arg NEW_RELIC_LICENSE_KEY=${NEW_RELIC_LICENSE_KEY} .

push-remote:
	docker push localhost:32000/${IMAGE}:${TAG}
	
build:
	docker build -t ${IMAGE}:${TAG} -f docker/Dockerfile --build-arg NEW_RELIC_LICENSE_KEY=${NEW_RELIC_LICENSE_KEY} .

local:
	docker-compose -f docker/docker-compose.yaml -p ${PROJECT_NAME} up -d --build

k8s-configmap:
	kubectl create configmap ${PROJECT_NAME}-config --from-env-file=.env -n works01

k8s-apply: build
	-kubectl create namespace works01
	kubectl apply -n works01 -f k8s/

