from fastapi import FastAPI, Body, Depends

from app.model import UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt

import threading
from multiprocessing import Pool

app = FastAPI()

# temporary way to store user data, use db in production
users = []


# root of the api
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "this is the root URL"}


# create user and return jwt token
@app.post("/user/signup", tags=["jwt"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return sign_jwt(user.email)


# verify user credentials
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# login user and return jwt token
@app.post("/user/login", tags=["jwt"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {"error": "Wrong login details"}


# return the number raised to power 10
def power_ten(n, results=None):
    res = n ** 10
    if results:
        results[n] = res
    return res


# use multithreading to execute func
@app.get("/multithreading", dependencies=[Depends(JWTBearer())], tags=["tasks"])
async def multithreading() -> dict:
    threads = [None] * 10
    results = [None] * 10

    # ten threads calling func with different args
    for i in range(10):
        threads[i] = threading.Thread(target=power_ten, args=(i, results))
        threads[i].start()

    for i in range(10):
        threads[i].join()

    return {"result": results}


# use multiprocessing to execute func
@app.get("/multiprocessing", dependencies=[Depends(JWTBearer())], tags=["tasks"])
async def multiprocessing() -> dict:

    # utilizing 4 cores, if available
    with Pool(processes=4) as pool:
        results = pool.map(power_ten, range(10))

    return {"result": results}
