from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class MyClass(str, Enum):
    value1 = "x"
    value2 = "xx"
    value3 = "xxx"


@app.get("/new/{myvalue}")
async def myFreakingFunc(myvalue: MyClass):
    x = "THIS IS FREAKING CRAZY"
    if myvalue == MyClass.value1:
        return {"myvalue": myvalue, "resp": "ooh boy"}
    elif myvalue == MyClass.value2:
        return {"myvalue": myvalue, "resp": "holy guacamole"}
    else:
        return "rip in pepperoni"

    return x
