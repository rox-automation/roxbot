#!/bin/bash

set -e

source config.sh

docker run -it --rm -p 8000:8000 $IMG_NAME
