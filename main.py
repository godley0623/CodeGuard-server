import random
import os
from models import Encrypt, Decrypt, Email
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import smtplib
from email.mime.text import MIMEText
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
    return {"message": MIMEText(generatePassword(), 'plain', 'utf-8')}

@app.post("/encrypt")
async def encrypt(encrypt: Encrypt):
    return {"message": encryptPassword(encrypt.encrypt)}

@app.post("/decrypt")
async def decrypt(decrypt: Decrypt):
    return {"message": decryptPassword(decrypt.decrypt)}

@app.post("/email")
async def email(email: Email):
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    port = 587 # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "codeguardpass@gmail.com"
    receiver_email = email.email 
    password = EMAIL_PASSWORD
    message = MIMEText(f"Subject: Your Generated Password\n\n{email.passwords}", "plain", "utf-8")

    #context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Email was sent")

    return {"message": "email sent successfully"}
