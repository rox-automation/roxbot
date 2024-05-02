# ROXBOT - a Pythonic robotics toolkit

## What is this repo?

This repository provides a series of examples and reusable library code for building robotic systems.
Common use case is an AGV, navigating with an RTK-GPS module.


## What about ROS?

Well, ROS2 has some nice concepts, but it can be complex and complicated. Besides, ROS is C++ centric, which makes it a bit old-fashioned. Another shortcoming is a large codebase that has not been widely tried and tested in real world applications.

## What is `Roxbot`?

*Roxbot* aspires to be a more pythonic way of programming robotics.

It follows these key principles:

* **KISS (keep it simple, stupid)**: - let's make robotics easier by reducing complexity.
* **Less Code Equals Fewer Problems:** - keep codebase small and portable
* **Don't reinvent the wheel** - leverage robust existing technologies. Think of `asyncio`, `Docker` etc.


## Concepts

ROXBOT takes familiar ideas from ROS2 and makes them easier to use and more Python-friendly:

- **Nodes**: These are small, focused classes that perform specific tasks within the robotics application. For example, one Node might manage sensor data while another controls a motor.

- **Interfaces**: These are standardized formats that ensure consistent data exchange between Nodes. This makes it easy for different parts of your project to communicate and work together effectively.

- **Subsystems**: This term refers to a group of Nodes that work together to perform a broader function like motion control or data logging. These subsystems can be packaged into Docker containers for easy deployment and scaling.

- **System**: This is the complete set of subsystems working together as a whole, forming a fully functional robotic system. We manage these as a Docker stack to ensure they are robust and scalable.


## Development workflow

### Prerequisites

* VSCode with devcontainer extension intalled
* `invoke` - python automation tool (`pip install invoke`)
* `docker`

### Working in devcontainer

This repository provides a `.devcontainer` environment that can be used in VSCode. For more information, read [VSCode containers docs](https://code.visualstudio.com/docs/devcontainers/containers)

The source for devcontainer image is located in `docker/dev`. It is built by github actions and hosted at `ghcr.io/rox-automation/roxbot:latest`


### CI

`ci_script.sh` executes linting and testing steps. This script can be run from a devcontainer or in a CI environment.
CI can be run in these ways:

* on *host* machine, run `invoke ci`. This will build a CI docker container, copy source code into it an run it. Because of caching, this is the fastest way to run ci in a clean envirionment.
* in *devcontainer* run `./ci_script.sh`.
* automated CI with github actions: TODO
