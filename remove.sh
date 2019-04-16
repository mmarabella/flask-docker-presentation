docker rm $(docker ps -a -q)
docker rmi flaskdockerapp_web
