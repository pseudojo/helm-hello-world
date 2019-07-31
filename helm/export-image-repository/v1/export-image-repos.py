#!/usr/bin/env python

import sys
import yaml


def get_image_fullname(image):
    if 'repository' in image and 'tag' in image:
        if image['repository'] is not None and image['tag'] is not None:
            return image['repository'] + ':' + str(image['tag'])

def filter_func(item):
    key = item[0]
    value = item[1]

    if type(value) == dict and 'image' in value:
        image = value['image']
        if image['repository'] is not None:
            return key + ' : ' + get_image_fullname(image)

# main start
chart = []

if len(sys.argv) == 1:
    print("must input argument : <filename>")
    exit(1)

with open(sys.argv[1], 'r') as stream:
    try:
        data = yaml.safe_load(stream)
        # test data
        # print(data)

        # test images
        # print("Main chart image : " + data["image"]["repository"] + ":" + str(data["image"]["tag"]))
        if 'image' in data :
            main_chart_image = get_image_fullname(data['image'])
            if main_chart_image is not None :
                chart.append('<main-chart> : ' + get_image_fullname(data['image']))

    except yaml.YAMLError as exc:
        print('Error: ' + exc)

chart.extend(
    filter(lambda x: x is not None, map(filter_func, data.items()))
)

print str(yaml.dump(chart, default_flow_style=False)).replace('\'', '')
