#!/bin/bash

# usage : get-chart-values.sh <release-name> <export-filename>
if [ $# -lt 2 ]; then
  echo 'usage : get-chart-values.sh <release-name> <export-filename>'
  exit 1
fi

helm get values --all $1 > $2

