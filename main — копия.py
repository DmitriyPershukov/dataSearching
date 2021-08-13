import struct, os
import json

from decimal import Decimal

typeArra= {"float":["f", 4], "int":["i", 4], "long long": ["q", 8], "double": ["d", 8]}
searchingtype ="double"
counterLength = 32

with open('390393_16-21-00.tdata','rb') as file:
    result = []
    byteStorer = file.read()
    counter = 0
    binarySize = 4
    bytetorerlen = os.stat('390393_16-21-00.tdata').st_size

    n = 0
    for o in typeArra:
        result.append({o: []})
        letter = typeArra[o][0]

        for p in range(0, typeArra[o][1]):
            counter = 0
            firs = 0
            coun = 0
            fourBytesStorer = b""
            passing = False
            for j in  range(p, bytetorerlen):
                coun = coun + 1
                fourBytesStorer +=  bytes([byteStorer[j]])
                if coun == typeArra[o][1]:
                    data = struct.unpack(letter, fourBytesStorer)
                    coun = 0
                    fourBytesStorer = b""
                    if str(data)[1:-2] == "nan":
                        number = -2
                    else:
                        number = float(str(data)[1:-2])
                    gi = bytetorerlen
                    if number >= 0:
                        counter = counter + 1
                        if not passing:
                            firs = j
                        passing = True
                    elif number <0 or j ==gi:
                        passing = False
                        if counter >= counterLength:
                            result[n][o].append({"pos": j, "len": counter})
                        counter = 0
        n +=1
    f = open("float.txt", "a")
    for ip in result:   
        f.write(json.dumps(ip))
        f.write()
