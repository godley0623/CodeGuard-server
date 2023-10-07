import random
from models import Encrypt, Decrypt
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,  # Allow sending cookies with requests
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers in the request
)

@app.get("/generate")
async def root():
    return {"message": generatePassword()}

@app.post("/encrypt")
async def encrypt(encrypt: Encrypt):
    return {"message": encryptPassword(encrypt.encrypt)}

@app.post("/decrypt")
async def decrypt(decrypt: Decrypt):
    return {"message": decryptPassword(decrypt.decrypt)}

