from fastapi import FastAPI,Depends,HTTPException
from schemas import Todo as TodoSchema,TodoCreate
from sqlalchemy.orm import Session
from database import sessionLocal,Base,engine
from models import Todo


Base.metadata.create_all(bind=engine)
app=FastAPI()


#Dependency for DB session
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
            


#POST -Create TODO Task

'''to create a route'''
@app.post("/todos",response_model=TodoSchema)
def create(todo:TodoCreate,db:Session=Depends(get_db)): #json as passed as parameter and json to py obj-session as parameter
    db_todo=Todo(**todo.dict()) # converting pandatic dtype to dict and unpack it
    db.add(db_todo) # add that task to db
    db.commit() # save that change
    db.refresh(db_todo) # to create id
    return db_todo
    
    
#get all Todo 
@app.get("/todos",response_model=list[TodoSchema])
def read_todos(db:Session=Depends(get_db)):
    return db.query(Todo).all()
      
      
#to get single todo
@app.get("/todos/{todo_id}",response_model=TodoSchema)
def read_todo(todo_id:int,db:Session=Depends(get_db)):
    todo= db.query(Todo).filter(Todo.id == todo_id).first() 
    if not todo:
        raise HTTPException(status_code=404,detail="Task not found")
    return todo
           

#PUT- update todo
@app.put("/todos/{todo_id}",response_model=TodoSchema)
def update_todo(todo_id:int,updated:TodoCreate,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id == todo_id).first() 
    if not todo:
        raise HTTPException(status_code=404,detail="Task not found")
    for key, val in updated.dict().items():
        setattr(todo,key,val) 
    db.commit()
    db.refresh(todo)
    return todo
 
#DELETE- delete todd
@app.delete("/todos/{todo_id}") 
def del_task(todo_id:int,db:Session=Depends(get_db)):  
    todo=db.query(Todo).filter(Todo.id == todo_id).first() 
    if not todo:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(todo)
    db.commit()
    return {"detail":"task has been deleted Successfully"}
    
           
      
    
