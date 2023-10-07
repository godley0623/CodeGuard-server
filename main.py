import random
from models import Encrypt, Decrypt
from fastapi import FastAPI
from encryptDecrypt import fullEncryption, fullDecryption

def generatePassword():
    seed = f'{random.randrange(1000, 10000000000)}'
    password = fullEncryption(100, 10, seed)

    return ''.join(password)

def encryptPassword(password):
    return fullEncryption(150, 10, password)

def decryptPassword(encodedPassword):
    return fullDecryption(10, encodedPassword)

app = FastAPI()

@app.get("/generate")
async def root():
    return {"message": generatePassword()}

@app.post("/encrypt")
async def encrypt(encrypt: Encrypt):
    return {"message": encryptPassword(encrypt.encrypt)}

@app.post("/decrypt")
async def decrypt(decrypt: Decrypt):
    return {"message": decryptPassword(decrypt.decrypt)}

