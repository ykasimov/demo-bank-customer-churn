SERVICE_NAME=demo-serving
MODEL_PATH="model/clf-model"
ECR="ecr"
REGISTRY_HOST="342840881361.dkr.ecr.us-east-2.amazonaws.com/mlem-test"
REGISTRY_REGION="us-east-2"
REGISTRY_ACCOUNT="342840881361"
IMAGE_NAME="mlem-test"

mlem deploy run kubernetes $SERVICE_NAME --model $MODEL_PATH --registry $ECR --registry.account $REGISTRY_ACCOUNT --registry.region $REGISTRY_REGION --registry.host $REGISTRY_HOST --image_name $IMAGE_NAME --service_type loadbalancer

