from schema.common import *

class RequestSchema_Signup(BaseModel):
    username :str
    email:str|None = None
    password :str 


class RequestSchema_Login(BaseModel):
    username : str
    password : str 


class ResponseSchema_Signup(BaseModel):
    username :str
    email:str|None = None
