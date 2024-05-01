.PHONY: list, clean, lint, test, build

SHELL := /bin/bash

UID := $(shell id -u)
GID := $(shell id -g)
USERNAME := $(shell id -u -n)

MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MKFILE_DIR := $(dir $(MKFILE_PATH))

CI_IMG := roxbot-ci

list:
	@cat Makefile

clean:
	rm -rf dist build venv public public

lint:
	ruff check src
	mypy src

test:
	pytest --cov=src --cov-report term-missing tests


build: clean
	python -m build
	# display package contents
	tar -tzf dist/*.tar.gz


ci:  # run CI locally in a docker container
	docker build -t $(CI_IMG) -f docker/Dockerfile.ci .
	docker run $(CI_IMG)
