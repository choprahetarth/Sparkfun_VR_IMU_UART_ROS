Configuration of Saprkfun VR IMU BNO080 without using Arduino
Just Plug and Play!

## Steps Required for Use

- Connect the IMU
- Paste the serial_uart_rvc_ros.py file to a package
- catkin_make
- rosrun <package_name> serial_uart_rvc_ros


## Working Demo
![Working](https://raw.githubusercontent.com/choprahetarth/Sparkfun_VR_IMU_UART_ROS/master/ezgif-3-f08b2f45a125.gif)

## TO DO -
- Filter the data incoming from the IMU by applying a Kalman/Complimentary Filter
