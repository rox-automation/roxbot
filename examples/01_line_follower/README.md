# Basic line follower example


```mermaid

graph TD
    controller_node --> |"(Vl,Vr)"|diffdrive_node
    diffdrive_node --> |"(Sl,Sr)"| odometry_node
    odometry_node -->|"(x,y,phi)"|controller_node

```

The system consists of 3 nodes:

* **controller** - uses  pure pursuit control algorithm to follow a line along x-axis
* **diffdrive** - simulates a differential drive robot
* **odometry** - keeps track of robot orientation based on dead reckoning


**Note:** we are assuming perfect odometry tracking here. In real world, this is not the case and odometry values are subject to drift. To solve this, sensor fusion techiques are often used like particle filters or Kalman filter.
