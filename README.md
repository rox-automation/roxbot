# ROXBOT - a KISS (Keep It Simple, Stupid) Robotics Framework

## About

ROS is a big name in robotics, known for its powerful but complex features. ROXBOT aims to simplify this by integrating modern, streamlined technologies like Docker, asyncio, and pydantic. This approach makes ROXBOT not only easier to use but also more robust and efficient.

Our project demonstrates this approach through a functional model of an RTK-GPS guided autonomous vehicle.

## Concepts

ROXBOT takes familiar ideas from ROS2 and makes them easier to use and more Python-friendly:

- **Nodes**: These are small, focused classes that perform specific tasks within the robotics application. For example, one Node might manage sensor data while another controls a motor.

- **Interfaces**: These are standardized formats that ensure consistent data exchange between Nodes. This makes it easy for different parts of your project to communicate and work together effectively.

- **Subsystems**: This term refers to a group of Nodes that work together to perform a broader function like motion control or data logging. These subsystems can be packaged into Docker containers for easy deployment and scaling.

- **System**: This is the complete set of subsystems working together as a whole, forming a fully functional robotic system. We manage these as a Docker stack to ensure they are robust and scalable.
