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



def linearSearch(arr, x):
    counter = 0  
    while counter < len(arr):
        if arr[counter] == x:
            results.append(counter) 
            counter = counter +1
        else:
            counter = counter +1
    return results


#def namingFunction():
#    counter = 0 
#    while(counter < 2):
#        counter = counter+1
#        discardValueFlag = 1
#    if (discardValueFlag == 1 )

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
                        print("i came here")
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
                    print(part3)
                    namingFunction()
                    part3=[]
                    additionCounter = 0 
            results = []
            part=[]
            part2=[]
            seq = []
            count = 0 
ser.close()
