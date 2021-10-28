import time
from typing import Dict

import jwt
from decouple import config


# load secrets from env
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# return generated jwt token
def token_response(token: str):
    return {"access_token": token}


# sign jwt string
def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


# decode jwt string
def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
