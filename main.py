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
    byte = file.read(1)
    
    while byte != b"":
        byteStorer.append(byte)
        byte = file.read(1)

    bytetorerlen = len(byteStorer)
    for j in  range(bytetorerlen):
        byteStore = []
        for p in range(32):
            fourByteStorer = b""
            offset = 4 * p
            for i in range(j +offset, j + 4 + 4 * p):
                fourByteStorer += byteStorer[i]
            data = struct.unpack('f', fourByteStorer)
            if str(data)[1:-2] == "nan":
                number = -3
            else:
                number = float(str(data)[1:-2])
            byteStore.append(number)

        passing = True
        for i in byteStore:
            if i >=0 :
                passin = True
            else:
                passin = False
        if passin:
            fkr.write(str(j) + ",  ")
    f.close()
    fkr.close()
    fd.close()
