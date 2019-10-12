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
results =[]
part = []
count = 0
cNew = 0 
reserveBITCounter = 0
queueChecker = 1
position = 0 
initMappingCounter = 0
discardCount = 0 
mappingCounter = 1
checkingCounter = 1
#startLSBposition = 0
#startMSBposition = 0 
#startLSB2position = 0
startMSB2position = 0

#var = [header1,header2,header3,header4,index1,\
#    index2,yawLSB1,yawLSB2,yawMSB1,yawMSB2,pitchLSB1,\
#    pitchLSB2,pitchMSB,pitchMSB2,rollLSB1,rollLSB2,rollMSB1,\
#    rollMSB2,xAccelLSB1,xAccelLSB2,xAccelMSB1,xAccelMSB2,\
#    yAccelLSB1,yAccelLSB2,yAccelMSB1,yAccelMSB2,\
#    zAccelLSB1,zAccelLSB2,zAccelMSB1,zAccelMSB2,\
#    reserved1LSB1,reserved1LSB2,reserved1MSB1,reserved1MSB2,\
#    reserved2LSB1,reserved2LSB2,reserved2MSB1,reserved2MSB2,\
#    reserved3LSB1,reserved3LSB2,reserved3MSB1,reserved3MSB2,\
#    csumLSB1,csumLSB2, csumMSB1, csumMSB2]

def linearSearch(arr, x):
    counter = 0  
    while counter < len(arr):
        if arr[counter] == x:
            results.append(counter) 
            counter = counter +1
        else:
            counter = counter +1
    return results


while True:
    for c in ser.readline().hex():
        seq.append(c)
        count += 1
        if count == 38:
            discardCount = discardCount +1
            if discardCount > 20:
                linearSearch(seq,'a')
                discardCount = 21
            if len(results)==4 and checkingCounter==1:
                initMappingCounter = initMappingCounter+1 
            elif len(results)!=4 and checkingCounter==1:
                initMappingCounter = 0
            if (initMappingCounter > 1 and mappingCounter == 1):
                checkingCounter = 2
                mappingCounter = 2
                part = results
                startMSB2position = part[3]
#            if (checkingCounter ==2 and mappingCounter ==2):
            print (seq)
            results = []
            seq = []
            count = 0 
ser.close()


    
