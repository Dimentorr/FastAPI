from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from fastapi import Security

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from security import config

# from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from base64 import urlsafe_b64encode
import os
import hashlib


def encode_data(data: str):
    try:
        return hashlib.sha256(data.encode()).hexdigest()
    except Exception as e:
        print(e)
        return None


def create_api_token():
    return hashlib.new('sha512').hexdigest()
