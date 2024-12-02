# pybase64_reddy/__init__.py

import base64

def encode(data: str) -> str:
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode(data: str) -> str:
    try:
        decoded_bytes = base64.b64decode(data.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError("Invalid base64 input") from e
