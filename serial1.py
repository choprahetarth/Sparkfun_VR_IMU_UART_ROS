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

    

def mapped():
    if checkingCounter ==2:
        print ("i am being called")
        mappingCounter = 0

while True:
    for c in ser.readline().hex():
        seq.append(c)
        count += 1
        if count == 38:
            linearSearch(seq,'a')
            if len(results)==4 and checkingCounter==1:
                initMappingCounter = initMappingCounter+1 
            elif len(results)!=4 and checkingCounter==1:
                initMappingCounter = 0
            if (initMappingCounter > 4 and mappingCounter == 1):
                checkingCounter = 2
                print ("in here ")
            print (results)
            results = []
            seq = []
            count = 0 
ser.close()


    
