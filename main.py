from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def index():
    return {"data" : {
      "name": "Umair",  
    }}
    
@app.get("/about")
def about():
    return {"data": "About this api"}