Configuration of Saprkfun VR IMU BNO080 without using Arduino
Just Plug and Play!

## Steps Required for Use

- Connect the IMU
- Paste the serial_uart_rvc_ros.py file to a package
- catkin_make
- rosrun <package_name> serial_uart_rvc_ros


TO DO meanwhile:
1- Remove ROS from the vizualize code and run it separately.
2- Filter the data incoming from the IMU by applying a Kalman/Complimentary Filter
