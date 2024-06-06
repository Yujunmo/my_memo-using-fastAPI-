from schema.common import *


class RequestSchema_CreateMemo(BaseModel):
    title:str
    content:str

class RequestSchema_UpdateMemo(BaseModel):
    title:str|None = None
    content:str|None = None





class ResponseSchema_CreateMemo(BaseModel):
    title:str|None = None
    content:str|None = None    

class ResponseSchema_GetMemo(BaseModel):
    id:int
    title:str|None = None
    content:str|None = None

    class Config:
        from_attributes = True

class ResponseSchema_GetMemos(BaseModel):
    memos:List[ResponseSchema_GetMemo]

class ResponseSchema_UpdateMemo(BaseModel):
    title:str|None = None
    content:str|None = None
