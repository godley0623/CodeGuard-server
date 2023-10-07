import random
from fastapi import FastAPI
from encryptDecrypt import fullEncryption, fullDecryption

def generatePassword() :
    seed = f'{random.randrange(1000, 10000000000)}'
    password = fullEncryption(100, 10, seed)

    return ''.join(password)


app = FastAPI()

@app.get("/generate")
async def root():
    return {"message": generatePassword()}
