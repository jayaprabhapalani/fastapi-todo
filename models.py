from sqlalchemy import Column,Integer,String,Boolean
from database import Base;

'''As usual table handling(like django)'''

class Todo(Base):
    __tablename__="todo"
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    completed=Column(Boolean,default=False)
    
    