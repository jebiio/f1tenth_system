# f110_system
Drivers onboard f1tenth race cars. This branch is under development for migration to ROS2.

## Dependencies
1. ackermann_msgs [https://index.ros.org/r/ackermann_msgs/#foxy](https://index.ros.org/r/ackermann_msgs/#foxy)
2. urg_node [https://index.ros.org/p/urg_node/#foxy](https://index.ros.org/p/urg_node/#foxy)
3. joy [https://index.ros.org/p/joy/#foxy](https://index.ros.org/p/joy/#foxy)
3. vesc [TODO](TODO)

## TODOs
- [ ] port the bringup package to ROS2
- [ ] finish vesc imu implementation
- [ ] test urg_node on car
- [ ] test joy on car
- [ ] test bringup launch on car