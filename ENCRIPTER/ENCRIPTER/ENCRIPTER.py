import numpy as np
from random import *

# For Matrix

def Encript(str):
    M = [[randint(0,100), randint(0,100), randint(0,100)], 
         [randint(0,100), randint(0,100), randint(0,100)], 
         [randint(0,100), randint(0,100), randint(0,100)]]
    charArr = list(str)
    i = 0
    if len(charArr) % 3 != 0:
        while (i < len(charArr) % 3):
            charArr.append(' ')
            i += 1
    
    i = 0
    while i < len(charArr):
        charArr[i] = ord(charArr[i])
        i += 1

    i = 0
    while i < len(charArr) / 3:
        NEWARR = [charArr[i], charArr[i + 1], charArr[i + 2]]
        NEWARR = np.dot(np.array(NEWARR, dtype=float), np.array(M, dtype=float))
        charArr[i] = NEWARR[0] 
        charArr[i + 1] = NEWARR[1]
        charArr[i + 2] = NEWARR[2]
        i += 3

    charArr.append(M[0][0])
    charArr.append(M[0][1])
    charArr.append(M[0][2])
    charArr.append(M[1][0])
    charArr.append(M[1][1])
    charArr.append(M[1][2])
    charArr.append(M[2][0])
    charArr.append(M[2][1])
    charArr.append(M[2][2])
    return charArr

def Decript(charArr):
    a = charArr[len(charArr)-1]
    b = charArr[len(charArr)-2]
    c = charArr[len(charArr)-3]
    d = charArr[len(charArr)-4]
    e = charArr[len(charArr)-5]
    f = charArr[len(charArr)-6]
    g = charArr[len(charArr)-7]
    h = charArr[len(charArr)-8]
    i = charArr[len(charArr)-9]
    M = [[i, h, g],
         [f, e, d],
         [c, b, a]]

    charArr.pop() 
    charArr.pop() 
    charArr.pop() 
    charArr.pop() 
    charArr.pop() 
    charArr.pop() 
    charArr.pop() 
    charArr.pop() 
    charArr.pop()
    NM = np.linalg.inv(np.array(M))

    i = 0
    while i < len(charArr) / 3:
        NEWARR = [charArr[i], charArr[i + 1], charArr[i + 2]]
        NEWARR = np.dot(np.array(NEWARR, dtype=float), np.array(NM, dtype=float))
        charArr[i] = NEWARR[0] 
        charArr[i + 1] = NEWARR[1]
        charArr[i + 2] = NEWARR[2]
        i += 3

    i = 0
    while i < len(charArr):
        charArr[i] = chr(int(charArr[i]))
        i += 1

    return ''.join(charArr)

print("Hello World")
print(Encript("password"))
print(Decript(Encript("Hello World")))