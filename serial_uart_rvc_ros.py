#!/usr/bin/env python
import serial
import time
import sys
import rospy
import numpy as np
from sensor_msgs.msg import Imu
#from tf.transformations import quaternion_from_euler


ser = serial.Serial(
    port='/dev/ttyUSB1',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)


#this will store the line
x=1
seq = []
results =[]
part = []
part2 = []
part3=[]
count = 0
cNew = 0
reserveBITCounter = 0
additionCounter =1
queueChecker = 1
position = 0
initMappingCounter = 0
discardCount = 0
mappingCounter = 1
checkingCounter = 1
startLSBposition = 0
positionIncrement = 0
initialPositionCounter = 0
shiftingCounter = 1
nextArrayCounter = 0
alternateCounter = 0
INDEX=0
YAW1=0
YAW2=0
PITCH1=0
PITCH2=0
ROLL1=0
ROLL2=0
XACCEL1=0
XACCEL2= 0
YACCEL1=0
YACCEL2=0
ZACCEL1=0
ZACCEL2=0
YAW=0
PITCH=0
ROLL=0
XACCEL=0
YACCEL=0
ZACCEL=0
yawMultiplier = 1
dataAvailableCounter = 0
pitchMultiplier = 1
rollMultiplier = 1
quaternions_final = [0,0,0,0]


def linearSearch(arr, x):
    counter = 0
    while counter < len(arr):
        if arr[counter] == x:
            results.append(counter)
            counter = counter +1
        else:
            counter = counter +1
    return results

def euler_to_quaternion(r, p, y):
        qx = np.sin(r/2) * np.cos(p/2) * np.cos(y/2) - np.cos(r/2) * np.sin(p/2) * np.sin(y/2)
        qy = np.cos(r/2) * np.sin(p/2) * np.cos(y/2) + np.sin(r/2) * np.cos(p/2) * np.sin(y/2)
        qz = np.cos(r/2) * np.cos(p/2) * np.sin(y/2) - np.sin(r/2) * np.sin(p/2) * np.cos(y/2)
        qw = np.cos(r/2) * np.cos(p/2) * np.cos(y/2) + np.sin(r/2) * np.sin(p/2) * np.sin(y/2)
        return [qx, qy, qz, qw]

def talker(quat1,quat2,quat3,quat4,accel1,accel2,accel3):
    pub = rospy.Publisher('imuPublisher01', Imu, queue_size=10)
    rospy.init_node('Imu_Publisher', anonymous=True)
    imu_msg = Imu()
    imu_msg.linear_acceleration.x = accel1
    imu_msg.linear_acceleration.y = accel2
    imu_msg.linear_acceleration.z = accel3
    imu_msg.angular_velocity.x = 0
    imu_msg.angular_velocity.y = 0
    imu_msg.angular_velocity.z = 0
    imu_msg.orientation.x = quat1
    imu_msg.orientation.y = quat2
    imu_msg.orientation.z = quat3
    imu_msg.orientation.w = quat4
    imu_msg.header.stamp = rospy.Time.now()
    imu_msg.header.frame_id = "IMU"
    pub.publish(imu_msg)

def twos_complement(hexstr,bits):
    value = int(hexstr,16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

def namingFunction(array1):
    INDEX = array1[4]+array1[5]
    YAW1 = array1[6]+array1[7]
    YAW2 = array1[8]+array1[9]
    PITCH1 = array1[10]+array1[11]
    PITCH2 = array1[12]+array1[13]
    ROLL1 = array1[14]+array1[15]
    ROLL2 = array1[16]+array1[17]
    XACCEL1 = array1[18]+array1[19]
    XACCEL2 = array1[20]+array1[21]
    YACCEL1 = array1[22]+array1[23]
    YACCEL2 = array1[24]+array1[25]
    ZACCEL1 = array1[26]+array1[27]
    ZACCEL2 = array1[28]+array1[29]
    YAW = (0.01*(twos_complement(YAW1,8)) + twos_complement(YAW2,8))
    yawMultiplier = 2.5069637883008 if YAW < 0 else 2.5423728813559
    YAW = YAW * yawMultiplier
    PITCH = (0.01 * twos_complement(PITCH1,8)) + twos_complement(PITCH2,8)
    pitchMultiplier = 2.4861878453038 if PITCH < 0 else 2.5495750708211
    PITCH = PITCH * pitchMultiplier
    ROLL = (0.01 * twos_complement(ROLL1,8)) + twos_complement(ROLL2,8)
    rollMultiplier = 2.5104602510462 if ROLL < 0 else 2.5423728813559
    ROLL = ROLL * rollMultiplier
    XACCEL = 0.001 * twos_complement(XACCEL1,8) + twos_complement(XACCEL2,8)
    YACCEL = 0.001 * twos_complement(YACCEL1,8) + twos_complement(YACCEL2,8)
    ZACCEL = 0.001 * twos_complement(ZACCEL1,8) + twos_complement(ZACCEL2,8)
    if dataAvailableCounter == 1:
        quaternions_final = euler_to_quaternion(ROLL,PITCH,YAW)
        talker(quaternions_final[0],quaternions_final[1],quaternions_final[2],quaternions_final[3],XACCEL,YACCEL,ZACCEL)
    print("Yaw - ", round(YAW,7), "Pitch - ", round(PITCH,7), "Roll - ", round(ROLL,7), "Accelerations - ", round(XACCEL,7),round(YACCEL,7),round(ZACCEL,7))
    if rospy.is_shutdown():
        exit()
    return ZACCEL2, ZACCEL1,YACCEL1, YACCEL2, XACCEL1, XACCEL2,ROLL1,ROLL2,PITCH1,PITCH2,YAW1,YAW2,INDEX,YAW,PITCH,ROLL,XACCEL,YACCEL,ZACCEL

while True:
    for c in ser.readline().hex():
        seq.append(c)
        count += 1
        if count == 38:
            discardCount = discardCount +1
            if discardCount > 20:
                linearSearch(seq,'a')       #started the technique to check the initial position
                discardCount = 21
            if len(results)==4 and checkingCounter==1:
                initMappingCounter = initMappingCounter+1
            elif len(results)!=4 and checkingCounter==1:
                initMappingCounter = 0
            if (initMappingCounter > 1 and mappingCounter == 1):
                checkingCounter = 2
                mappingCounter = 2
                startLSBposition = results[0]                      #after this has been done, the starting position is returned
            if (checkingCounter ==2 and mappingCounter ==2):
                alternateCounter = alternateCounter +1
                while shiftingCounter == 1:
                    if (alternateCounter % 2 != 0):
                        break
                    initialPositionCounter = startLSBposition + positionIncrement
                    if (len(seq)-initialPositionCounter == 0):
                        shiftingCounter = 0
                        nextArrayCounter = 1
                        positionIncrement = 0
                    else:
                        part.append(seq[initialPositionCounter])
                        part3.append(seq[initialPositionCounter])
                        positionIncrement= positionIncrement +1
                additionCounter = additionCounter+1
                while nextArrayCounter == 1:
                    if (alternateCounter % 2 == 0):
                        break
                    if (x <= startLSBposition):
                        part2.append(seq[x-1])
                        part3.append(seq[x-1])
                    else:
                        nextArrayCounter = 2
                        x = 0
                        shiftingCounter = 1
                    x = x +1
                if (additionCounter == 2):
                    if (len(part3) == 0):
                        pass
                    else:
                        dataAvailableCounter =1
                        namingFunction(part3)
                    part3=[]
                    additionCounter = 0
            results = []
            part=[]
            part2=[]
            seq = []
            count = 0
ser.close()
