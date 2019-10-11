import serial
import time 

ser = serial.Serial(
    port='/dev/cu.usbserial-A5XK3RJT',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)


#this will store the line
seq = []
part = []
count = 0
cNew = 0 
reserveBITCounter = 0
queueChecker = 1

while True:
    for c in ser.readline().hex():
        if c == 'a' and queueChecker == 1:
            reserveBITCounter = reserveBITCounter + 1
        elif c != 'a' and queueChecker == 1:
            reserveBITCounter = 0
        if reserveBITCounter == 6:
            queueChecker = 0
            seq.append(c)
            count += 1
            if count == 38:
                print (seq)
                seq = []
                count = 0 
reserveBITCounter = 0 
queueChecker = 1
ser.close()