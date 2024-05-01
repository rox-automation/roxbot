# Mkdocs container

Used for building and serving docs with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)



## Usage

mount folder containing `mkdocs.yml` to `/docs` inside container and run.

example:

    docker run --rm -it -p 8010:8000 -v ${PWD}/test_docs:/docs <img_name>


## Demo

Image includes sample docs folder that can be biult and served right away.
Start it with `demo.sh`
