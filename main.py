import struct, os

NO_OF_CHARS = 256


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
    print(len(unique))

def islisEmpty(list):
    if len(list) != 0:
        return False
    else:
        return True
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

with open('390393_16-21-00.tdata', 'rb') as file:
    f = open("dfg.txt", "a")
    byte = file.read(1)
    count = 0
    p = "<?xm"
    patternLength = len(p)


    statetable = computeStateTable(p)
    byteStorer = b""
    state = 0

    brackets = []
    passingMetadata = False
    while byte != b"":


        character = str(struct.unpack('s', byte))[3]
        pattern = list(set(p))
        if any(character in pattern):
            character = 'anyCharacter'
        state = statetable[state][character]
        if state == patternLength:
            passingMetadata = True
            print(True)
            brackets.append('<')
        if passingMetadata:
            if islisEmpty(brackets):
                passingMetadata =False
            if character == '<':
                brackets.append('<')
            elif character == '>':
                brackets.pop()
        count = count + 1
        byteStorer = byteStorer + byte
        if count == 4:
            data = struct.unpack('f', byteStorer)
            count = 0
            f.write(str(data))
            byteStorer = b""
        byte = file.read(1)
    f.close()