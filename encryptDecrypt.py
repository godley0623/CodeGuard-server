import random

def EncryptDecrypt(message, key, mode):
    minValue = 32
    maxValue = 255
    combineKey = 0
    newMessage = ''
    keyTarget = 0
    placement = 0

    message = message.replace("\n", "[@LB@]")

    for k in key:
        combineKey += ord(k)
    for m in message:
        char = int(((ord(key[keyTarget])*8.9+combineKey)*ord(key[keyTarget])+placement)/255)
        char = int((char+ord(key[keyTarget])*2.5)/255+placement)
        newChar = ord(m)

        for i in range(char):
            if mode == 0:
                newChar += 1
            else:
                newChar -= 1
            if newChar > maxValue:
                newChar = minValue
            if newChar < minValue:
                newChar = maxValue

        newMessage = newMessage+chr(newChar)

        placement += ord(key[keyTarget]) + 9.25
        keyTarget += 1

        if keyTarget > len(key)-1:
            keyTarget = 0

        if placement > 255:
            placement = 0

    return newMessage.replace("[@LB@]", "\n")

def GenerateKey(numOfChr):
    if numOfChr < 100 or numOfChr%2 != 0:
        raise Exception("The key's string length must be 100 or higher and it must be an even integer.")

    key = ''

    for i in range(numOfChr):
        key = key+chr(random.randrange(32,256))

    return key

def AddKey2Encrypt(encrypt, key):
    keyLen = len(key)
    keyLenStr = str(keyLen)

    keyFirstHalf = key[0:int(keyLen/2)]
    keySecHalf = key[int((keyLen/2)*-1):]

    keyFirstHalfList = list(keyFirstHalf)
    keyFirstHalfList.insert(15, keyLenStr[0])
    keyFirstHalfList.insert(30, keyLenStr[1])
    keyFirstHalfList.insert(45, keyLenStr[2])
    keyFirstHalf = ''.join(keyFirstHalfList)

    return [keyFirstHalf, encrypt, keySecHalf]

def AddKey2Decrypt(encryptFused):
    encryptFusedList = list(encryptFused[0])

    encryptFusedList.pop(15)
    encryptFusedList.pop(30-1)
    encryptFusedList.pop(45-2)

    encrypt = encryptFused[1]
    key = ''.join(encryptFusedList)+encryptFused[2]

    return [encrypt, key]

def MultiEncrypt(num, message, key):
    encryptMessage = EncryptDecrypt(message, key, 0)
    while num > 0:
        encryptMessage = EncryptDecrypt(encryptMessage, key, 0)
        num -= 1

    return encryptMessage

def MultiDecrypt(num, message, key):
    decryptMessage = EncryptDecrypt(message, key, 1)
    while num > 0:
        decryptMessage = EncryptDecrypt(decryptMessage, key, 1)
        num -= 1

    return decryptMessage

def fullEncryption(keyLength, numOfEncryption, message):
    #print('----------------------------Encrypt----------------------------------------')
    genKey = GenerateKey(keyLength)
    enCode = MultiEncrypt(numOfEncryption, message, genKey)
    #print(enCode)
    #print('----------------------Encrypt with Key-------------------------------')
    enCodePlusKey = AddKey2Encrypt(enCode, genKey)
    #print(''.join(enCodePlusKey))
    return enCodePlusKey

def fullDecryption(numOfDecryption,enCodePlusKey):
    #print('--------------------------Decrypt-------------------------------------')
    deCodePlusKey = AddKey2Decrypt(enCodePlusKey)
    deCode = MultiDecrypt(numOfDecryption, deCodePlusKey[0], deCodePlusKey[1])
    return deCode

# keyLength = 100
# safetyNum = keyLength
# enCodeTalker = fullEncryption(keyLength, safetyNum, 'https://discord.gg/8whhazMR')
# fullDecryption(safetyNum, enCodeTalker)


