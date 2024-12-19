PROJECT_ID='qwiklabs-gcp-04-ce8906d9b765'
IMAGE_URI="gcr.io/$PROJECT_ID/horse-human:hypertune"
docker build ./ -t $IMAGE_URI
docker push $IMAGE_URI