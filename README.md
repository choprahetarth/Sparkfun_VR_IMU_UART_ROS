Configuration of Saprkfun VR IMU BNO080 without using Arduino
Just Plug and Play!



1- Connect the IMU
2- Paste the serial_uart_rvc_ros.py file to a package
3- catkin_make
4- rosrun <package_name> serial_uart_rvc_ros


TO DO meanwhile:
1- Remove ROS from the vizualize code and run it separately.
2- Filter the data incoming from the IMU by applying a Kalman/Complimentary Filter
