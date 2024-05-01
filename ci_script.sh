#!/bin/bash

# main CI script. Run in a docker container, locally or in github actions
# assuming all dependencies are installed

set -x

# pip install .[dev]
ruff check src
mypy src
pytest tests
