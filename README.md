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

## What goes where

* `examples` - collection of examples around building an example AGV
* `src` - library code


## Concepts

ROXBOT takes familiar ideas from ROS2 and makes them easier to use and more Python-friendly:

- **Nodes**: These are small, focused classes that perform specific tasks within the robotics application. For example, one Node might manage sensor data while another controls a motor.

- **Interfaces**: These are standardized formats that ensure consistent data exchange between Nodes. This makes it easy for different parts of your project to communicate and work together effectively.

- **Subsystems**: This term refers to a group of Nodes that work together to perform a broader function like motion control or data logging. These subsystems can be packaged into Docker containers for easy deployment and scaling.

- **System**: This is the complete set of subsystems working together as a whole, forming a fully functional robotic system. We manage these as a Docker stack to ensure they are robust and scalable.
