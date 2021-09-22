# f110_system
Drivers onboard f1tenth race cars. This branch is under development for migration to ROS2.

## Dependencies
1. ackermann_msgs [https://index.ros.org/r/ackermann_msgs/#foxy](https://index.ros.org/r/ackermann_msgs/#foxy)
2. urg_node [https://index.ros.org/p/urg_node/#foxy](https://index.ros.org/p/urg_node/#foxy)
3. joy [https://index.ros.org/p/joy/#foxy](https://index.ros.org/p/joy/#foxy)
3. vesc [TODO](TODO)
4. rosbridge_suite [https://index.ros.org/p/rosbridge_suite/#foxy-overview](https://index.ros.org/p/rosbridge_suite/#foxy-overview)

## Nodes launched in bringup
1. joy
2. joy_teleop
3. ackermann_to_vesc_node
4. vesc_driver_node
5. vesc_to_odom_node
6. throttle_interpolator.py
7. static transforms for frames
8. hokuyo_node (should switch to urg_node)
9. mux?
10. rosbridge_websocket.launch

## TODOs
- [ ] port the bringup package to ROS2
- [ ] finish vesc imu implementation
- [ ] test urg_node on car
- [ ] test joy on car
- [ ] test bringup launch on car
- [ ] test foxglove studio integration over rosbridge