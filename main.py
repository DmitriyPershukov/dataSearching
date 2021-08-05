import struct, os

from decimal import Decimal
def getNextState(pattern, state,nextCharacter):
    if nextCharacter == 'anyCharacter':
        return 0
    if state < len(pattern) and nextCharacter == pattern[state]:
        return state + 1

    i = 0
    for nextstate in range(state,0,-1):
        if pattern[nextstate-1] ==nextCharacter:
            while(i<nextstate-1):
                if pattern[i] != pattern[state-nextstate+1+i]:
                    break
                i+=1
            if i == nextstate-1:
                return nextstate
    return 0

def countUniqueChar(string):
    unique = []
    for char in string[::]:
        if char not in unique:
            unique.append(char)
            
def islisEmpty(list):
    if len(list) != 0:
        return False
    else:
        return True
def searchingSubString(state, pattern, stateTable, character ):
    patternLength = len(pattern)
    patternchars = list(set(pattern))
    if character not in patternchars:
            character = 'anyCharacter'
    state[0] = stateTable[state[0]][character]
    if state[0] == patternLength:
        print(True)
        return True
    else:
        return False
def computeStateTable(pattern):
    length = len(pattern)

    character = list(set(pattern))
    character.append('anyCharacter')
    stateTable = {}
    for i in range(0, length + 1):
        stateTable[i] = {}
        
    for state in range(length + 1):
        for x in character:
            z = getNextState(pattern, state, x)
            stateTable[state][x] = z
        
    return stateTable

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
#with open('390393_16-21-00.tdata',
with open('Новый текстовый документ.txt','rb') as file:
    f = open("float.txt", "a")
    fd = open("doubl.txt", "a")
    df = open("long long.txt", "a")
    fkr = open("long.txt", "a")
    byte = file.read(1)
    count= 0
    p = "<?xm"
    patternLength = len(p)


    statetable = computeStateTable(p)
    eightByteStorer = b""
    fourByteStorer = b""
    floatStartposition = [0]
    doubleStartPosition = [0]
    longlongStartPosition = [0]
    longStartPosition =[0]
    positionCounter = 0
    floaCounter = [0]
    doubleCounter= [0]
    longCounter =[0]
    state = [0]
    fState = [0]
    flagStateTable = {}

    sko = True
    recordWord = ""
    record = True
    passingmetadata = False
    searchingFlag = False
    while byte != b"":

        
        character = str(struct.unpack('s', byte))[3]
        if searchingSubString(state, p, statetable, character):

            passingmetadata = True
        if passingmetadata:
            if  not searchingFlag and character == '<':
                record = True
                recordWord = recordWord + "</"
            if record and str(struct.unpack('s', byte))[3] == " ":
                record = False
                recordWord += ">"
                searchingFlag = True
                flagStateTable = computeStateTable(recordWord)
            if record and str(struct.unpack('s', byte))[3] != " " and str(struct.unpack('s', byte))[3] != "<":
                recordWord = recordWord + str(struct.unpack('s', byte))[3]
            if searchingFlag:
                characteyu = str(struct.unpack('s', byte))[3]
                if searchingSubString(fState, recordWord, flagStateTable, characteyu):
                    searchingFlag = False
                    count = 0
                    passingmetaData = False
                    print(str(struct.unpack('s', byte))[3])
                    sko = True
        else:
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
                data = struct.unpack('f', fourByteStorer) 

                if str(data)[1:-2] == "nan":
                    number = "nan"
                else:
                    number = float(str(data)[1:-3])
                searchLongSequences(f,positionCounter, floatStartposition, floaCounter, number)
                count = 0
                data8 = struct.unpack('d', eightByteStorer)



                if str(data)[1:-2] == "nan":
                    number = "nan"
                else:
                    number = float(str(data8)[1:-2])
                searchLongSequences(fd ,positionCounter, doubleStartPosition, doubleCounter, number)
                fourByteStorer = b""
                eightByteStorer = b""
        byte = file.read(1)
        positionCounter = positionCounter +1
    f.close()
    fd.close()
    fkr.close()
