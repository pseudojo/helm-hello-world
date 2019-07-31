#!/usr/bin/env python
# coding=utf-8

import sys
import yaml
import copy


# Ref. : https://stackoverflow.com/a/23231459
def fltr_and_transform(node, vals, transformFunc = None, resultKey = None, deleteAfterTransformation = False):
    vals_with_result = copy.deepcopy(vals)
    vals_with_result.append(resultKey)

    if isinstance(node, dict):
        retVal = {}
        for key in node:
            if key in vals_with_result:
                 retVal[key] = copy.deepcopy(node[key])
            elif isinstance(node[key], list) or isinstance(node[key], dict):
                child = fltr_and_transform(node[key], vals, transformFunc, resultKey, deleteAfterTransformation)
                if child:
                    if isinstance(child, dict) and resultKey in child:
                        retVal[key] = child[resultKey]
                    else:
                        retVal[key] = child

    elif isinstance(node, list):
        retVal = []
        for entry in node:
            child = fltr_and_transform(entry, vals, transformFunc, resultKey, deleteAfterTransformation)
            if child:
                if isinstance(child, dict) and resultKey in child:
                    retVal.append(child[resultKey])
                else:
                    retVal.append(child)

    # finally
    if retVal:
        if transformFunc:
            retVal = transformFunc(retVal, vals, resultKey, deleteAfterTransformation)
        return retVal
    else:
        return None


def transformChartYaml(entry, combineKeys, resultKey, deleteAfterTransformation):
    # check validation
    if isinstance(entry, dict):
        for key, value in entry.items():
            if value is None:
                del entry[key]

    try:
        # option: delete after transform
        if deleteAfterTransformation:
            entry = entry[combineKeys[0]] + ':' + str(entry[combineKeys[1]])
        else:
            entry[resultKey] = entry[combineKeys[0]] + ':' + str(entry[combineKeys[1]])
    except:
        pass

    if deleteAfterTransformation and isinstance(entry, dict):
        for key in combineKeys:
            try:
                del entry[key]
            except:
                pass

    return entry


def reformat(images):
    mainChartImage = images['image']
    del images['image']

    chartImageList = {
        'chart': {
            'name': chartname,
            'image': mainChartImage
        },
        'subcharts': images
    }

    return chartImageList

# main
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("must input argument : <filename> <chartname>")
        exit(1)

    filename = sys.argv[1]
    chartname = sys.argv[2]

    with open(filename, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            print str(data) + '\r\n'

        except yaml.YAMLError as exc:
            print('Error: ' + exc)

    images = fltr_and_transform(data, ['repository', 'tag'], transformChartYaml, 'fullname', True)
    imageList = reformat(images)


    print yaml.dump(imageList, default_flow_style=False).replace('\'', '')

