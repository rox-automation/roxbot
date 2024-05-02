---
date: 2023-07-27
categories:
    - ROS2
draft: true

---

# Where ROS2 falls short

If you are into robotics, you just can't ignore ROS. In fact, ROS has become defacto standard platform
for robotics.
While it is widely agreed that ROS1 is not suitable for industrial applications, it's redesigned brother ROS2 is
not without its own shortcomings. I've been developing autonomous robots for a couple of years now. When I started
with my first robot, choosing ROS was logical, everybody else was using it.
I started with ROS2 Foxy and my first impression was very positive. But as the time went by, I felt that ROS system
was getting in the way instead of providing a decent solution for my robotics needs.   SStep by step I gradually moved
away from ROS to a pure Python system running in a Docker stack, resulting in a simpler system that is build upon
well-tested components.

<!-- more -->

In this article I'll share with you where I think that ROS gets in the way and provide a better working alternative.

But first, let's recap on what ROS actually is. It is a software framework providing:

1. inter-process communication
2. package management (deployment)
3. node management (launcing configuratoin etc.)

ROS provides more than that, but in essence these are the most important parts.

Inter-process communication is essential for creating a heterogenous asynchronous system.
Distributed system of ROS works well when operating within same subnet. Sending messages to a remote
system (or even communicating to host of a docker container) can be major pain. I've spent countless hours trying
to connect hosts on different subnets without success. And connecing nodes in separate (remote) subnets is just
not something that I have time for figuring it out. You'll need to start digging trhough documentation about communication layer,
do some math to calculate which ports are used for a domain id etc.

An alternative could be a centralized protocol, like MQTT. You know to what host and which port you need to connect. If something
does not work, troubleshooting is easy.


As for package management...


## Story in bullet points

* I develop preferably in Python, it enables me to build functionality faster with less code and provides access to a wealth of tools and packages.
* ROS has C++ as primary language, using Python is a second-class citizen.
* The way the code needs to be packaged is different from standard python packages. Why do we need `ros2 run ...` while an  executable can be installed on the system?
* ROS uses it's own custom and complex launch system. Systemd and docker stacks are much more mature and well designed solutions.
* Defining and compiling interfaces causes development overhead.
* Getting data across subdomains can be a major pain. An alternative could be a centralized protocol, like MQTT. You know to what host and which port you need to connect. If something
does not work, troubleshooting is easy.
* Performance - based on my benchmark ping-pong between two nodes in ROS is approximately 100 times slower than same system implemented with asyncio in pure Python.

Conclusion: for a Python-first system ROS is not optimal.
After working with ROS for a couple of years I found an architecture that works much better for me:

* The system is split in a number of subsystems, each running in a separate docker container. This achieves modularity and there are great mature tools for container management.
* Within each subsystem asyncio is used for running concurrent tasks. Inter-node communication is easy and blazing fast with queues. There is no risk of race conditions, that's a trait of
asyncio not running multiple threads.
* Subsystems communicate with each other through MQTT (mosquitto broker is running in a separate conainer). This is still much faster than sending messages through rclpy. Not sure
why, but the benchmark proves it.
