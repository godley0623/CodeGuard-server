from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Encrypt(BaseModel):
    encrypt: str

class Decrypt(BaseModel):
    decrypt: List[str]