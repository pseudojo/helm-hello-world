# How to build
docker build -t pseudojo/node-hello-world:0.1 .

# How to run
docker run -dt -p<REAL-MACHINE-EXPOSE-PORT>:8080 node-hello:0.1

ex)
docker run -dt -p9999:8080 pseudojo/node-hello-world:0.1

# How to test
curl localhost:9999

