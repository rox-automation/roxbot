#!/bin/bash
set -e
set -x

source config.sh

# Build the mkdocs image
docker build -t $IMG_NAME  .
