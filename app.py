from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#BAseModel help by pydantic - there are some basemodel designed in pydantic 


app = FastAPI()

class Tea(BaseModel):
    id:int 
    name:str
    origin:str

teas: List[Tea] = []

#fastapi works on Decoraters which are also know as super powers of fucntion #/tea #/tea_id

@app.get("/")
def read_root():
    return {"message":"welcoem to AVVROLT"}

@app.get("/teas")
def  get_teas():
    return teas

#post method to add teas and delte teas or modify teas.

@app.post("/teas")
def add_teas(tea:Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int , updated_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
    return {"error":"tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
           deleted =  teas.pop(index)
        return deleted
    return {"error":"tea not found"}


