import os
from datetime import timedelta

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRES_MINUTES = timedelta(minutes=int(os.environ.get('ACCESS_TOKEN_EXPIRES')))

