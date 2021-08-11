
import struct, os

import json

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

def get(i):
    return bytes([byte[i]])
with open('390393_16-21-00.tdata','rb') as file:
    f = open("float.txt", "a")
    result = []
    byteStorer = b""
    byteStorer = file.read()
    counter = 0
    binarySize = 4
    bytetorerlen = os.stat('390393_16-21-00.tdata').st_size
    for p in range(0, binarySize):
        counter = 0
        firs = 0
        coun = 0
        fourBytesStorer = b""
        passing = False
        for j in  range(p, bytetorerlen):
            coun = coun + 1
            fourBytesStorer +=  bytes([byteStorer[j]])
            if coun == binarySize:
                data = struct.unpack('f', fourBytesStorer)
                coun = 0
                fourBytesStorer = b""
                if str(data)[1:-2] == "nan":
                    number = -2
                else:
                    number = float(str(data)[1:-2])
                if number >= 0:
                    counter  == counter + 1
                    if not passing:
                        firs = j
                    passing = True
                else:
                    passing = False
                    if counter >= 32:
                         result.append({"pos": j, "len": counter})
                    counter = 0
    f.write(json.dumps(result))
    f.close()
