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
startLSBposition = 0
startMSBposition = 0 
startLSB2position = 0
startMSB2position = 0

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
            if (initMappingCounter > 2 and mappingCounter == 1):
                checkingCounter = 2
                print ("in here ")
                mappingCounter = 0
                startLSBposition = results[0]
                startMSBposition = results[1]
                startLSBposition = results[2]
                startLSB2position = results[3]
            print (results)
            print (startLSBposition)
            results = []
            seq = []
            count = 0 
ser.close()


    
