import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(dotenv_path='.env')

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRES_MINUTES = timedelta(minutes=int(os.environ.get('ACCESS_TOKEN_EXPIRES_MINUTES')))

KRYPTO_KEY = os.environ.get("CRYPT_KEY")
