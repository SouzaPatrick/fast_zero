from fastapi import FastAPI
from fast_zero.schemas import Message, UserSchema
from http import HTTPStatus

app = FastAPI()


@app.get("/", response_class=Message)
def read_root():
    return {"message": "Olá Mundo!"}

@app.post("/users", status_code=HTTPStatus.OK, response_class=UserSchema)
def 