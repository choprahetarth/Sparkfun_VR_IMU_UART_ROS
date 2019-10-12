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
x=0
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
positionIncrement = 0 
initialPositionCounter = 0
shiftingCounter = 1
nextArrayCounter = 0
#startMSBposition = 0 
#startLSB2position = 0
#startMSB2position = 0

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
                alternateCounter = 0
                alternateCounter = alternateCounter +1
                while shiftingCounter == 1:
                    if (alternateCounter % 2 != 0):
                        break
                    initialPositionCounter = startLSBposition + positionIncrement    # a = startposition + x
                    if (len(seq)-initialPositionCounter == 0):
                        shiftingCounter = 0
                        nextArrayCounter = 1
                        positionIncrement = 0
                    else:
                        part.append(seq[initialPositionCounter])
                        positionIncrement= positionIncrement +1
                while nextArrayCounter == 1:
                    if (alternateCounter % 2 == 0):
                        break
                    if (x <= startLSBposition):
                        part.append(seq[x])
                    else:
                        nextArrayCounter = 2
                        x = 0
                        shiftingCounter = 1
                    x = x +1
            print(seq)
            print(part)
            part = []            
            results = []
            seq = []
            count = 0 
ser.close()


    
