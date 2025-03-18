from fastapi import FastAPI

app = FastAAPI()

@app.get("/hello")
def hello_world():

    return{"message" : "hello world"}