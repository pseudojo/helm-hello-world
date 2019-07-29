# How to build
docker build -t pseudojo/node-hello-world:0.1 .
docker push pseudojo/node-hello-world:0.1

# How to run
docker run -dt -p<REAL-MACHINE-EXPOSE-PORT>:8080 node-hello:0.1

ex)
docker run -dt -p9999:8080 pseudojo/node-hello-world:0.1

# How to test
curl localhost:9999

# Etc...
## How to use docker group
```
## Ref. : https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user
## Set group in current user...
sudo groupadd docker
sudo usermod -aG docker $USER

## how to use docker group
newgrp docker
docker ps -a
docker images 
...
```


