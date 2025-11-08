from pydantic import BaseModel

'''Pydantic package  used for
       -validation of datatypes in db fields
       -parsing raw data to obj's
       -serializes(py objs to json)
       -error handling
       exactly like django(after creating model--serialzing here)
       '''

'''Why too many schemas---so basically we need diff json acc to the api(get/put/patch/del) 
so based on the use case we creating diff schemas to access the data via api as json'''

class TodoBase(BaseModel):
    title:str
    description:str | None = None
    completed:bool =False

# to create a task 
class TodoCreate(TodoBase):
    pass  

# to get response
class Todo(TodoBase):
    id:int 
    class Config:
        orm_mode=True  #to convert it from py obj to json
    
    