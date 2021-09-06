## Description 
While working on the a robotics research project involving ROS, I noticed that the IMU I have been using, namely ["Sparkfun's VR IMU"](https://www.sparkfun.com/products/14686) did not have a ROS Package. Hooking it up to an Arduino board, and adding publishers and subscribers seemed to do the trick, but a special UART-RVC mode worked directly using an FTDI Interface. And hence, I developed a small script to make sure the IMU runs without using an Ardunio.
Just Plug and Play!

## Hardware Setup
[Kindly Refer Here](https://github.com/choprahetarth/Sparkfun_VR_IMU_UART_ROS/blob/master/FTDI.jpg)

## Steps Required for using the ROS Version
- Connect the IMU
- Paste the serial_uart_rvc_ros.py file to a package
''' 
catkin_make 
'''
- rosrun <package_name> serial_uart_rvc_ros

## Steps to use the Non-ROS Version (just for visualizing)
- Connect the IMU
- python3 vizualize.py


## Working Demo
![Working](https://raw.githubusercontent.com/choprahetarth/Sparkfun_VR_IMU_UART_ROS/master/ezgif-3-f08b2f45a125.gif)

## TO DO -
- Filter the data incoming from the IMU by applying a Kalman/Complimentary Filter.
- Using DeQueue, increase the performance of the code.
