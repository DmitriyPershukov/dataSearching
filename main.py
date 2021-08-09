import struct, os

from decimal import Decimal 
            
def islisEmpty(list):
    if len(list) != 0:
        return False
    else:
        return True

def searchLongSequences(f, positionCounter, startingPositionCounter, count, number):
    if number == "nan":
        count[0] = 0
        return
    if number >= 0:
        count[0] = count[0] +1
        if count[0] == 0:                            
            startingPositionCounter[0] = positionCounter
    
        if count[0] >= 32:
            f.write(str(startingPositionCounter[0]) + ", ")
    else:
        count= 0
with open('390393_16-21-00.tdata','rb') as file:
    f = open("float.txt", "a")
    df = open("long long.txt", "a")
    fkr = open("long.txt", "a")
    byte = file.read(1)
    count= 0         

    eightByteStorer = b""
    fourByteStorer = b""
    floatStartposition = [0, 0, 0, 0]
    doubleStartPosition = [0]
    longlongStartPosition = [0]
    longStartPosition =[0, 0 ,0 0]
    positionCounter = 0
    floaCounter = [0]
    doubleCounter= [0]
    longCounter =[0]
    counter = 0
    
    while byte != b"":
        count += 1
        fourByteStorer = fourByteStorer + byte
        eightByteStorer += byte
        if count == 4:

            data = struct.unpack('f', fourByteStorer)
                    
                if str(data)[1:-2] == "nan":
                    numbe = "nan"
                else:
                    numbe = float(str(data)[1:-2])

                searchLongSequences(fkr,positionCounter, longStartPosition, longCounter, numbe)
                data = struct.unpack('l', fourByteStorer)
                if str(data)[1:-2] == "nan":
                    number = "nan"
                else:
                    number = float(str(data)[1:-2])

                searchLongSequences(f,positionCounter, floatStartposition, floaCounter, number)
                fourByteStorer = b""
        if count == 8:
        byte = file.read(1)
        positionCounter = positionCounter +1
    f.close()
    fd.close()
    fkr.close()
