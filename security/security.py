import hashlib


def encode_data(data: str):
    return hashlib.sha256(data.encode()).hexdigest()


def create_api_token():
    return hashlib.new('sha512').hexdigest()
