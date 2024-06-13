#!/bin/bash

# main CI script. Run in a docker container, locally or in github actions
# assuming all dependencies are installed

set -e

python --version

pip install .
pip install .[dev]
pylint -E src tests
mypy src
pytest --cov=src --cov-report term-missing tests
