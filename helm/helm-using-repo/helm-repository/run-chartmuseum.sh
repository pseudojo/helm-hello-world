#!/bin/bash

docker run --rm -dt \
  -p 8080:8080 \
  -v /tmp/charts:/charts \
  -e DEBUG=true \
  -e STORAGE=local \
  -e STORAGE_LOCAL_ROOTDIR=/charts \
  chartmuseum/chartmuseum

# test
#curl http://localhost:8080

# add local repo
helm repo add chartmuseum http://localhost:8080

