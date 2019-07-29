#!/usr/bin/env python

import sys
import yaml

if len(sys.argv) == 1:
    print("must input argument : <filename>")
    exit(1)

with open(sys.argv[1], 'r') as stream:
    try:
        data = yaml.safe_load(stream)
        # test data
        #print(data)
        
        # test images
        print("Main chart image : " + data["image"]["repository"] + ":" + str(data["image"]["tag"]))
        
    except yaml.YAMLError as exc:
        print(exc)
