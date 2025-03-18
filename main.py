from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/quote1")
def quote1():
    return {"quote": "The only way to do great work is to love what you do. - Steve Jobs"}

@app.get("/quote2")
def quote2():
    return {"quote": "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer"}

@app.get("/quote3")
def quote3():
    return {"quote": "Believe you can and you're halfway there. - Theodore Roosevelt"}

@app.get("/quote4")
def quote4():
    return {"quote": "It does not matter how slowly you go as long as you do not stop. - Confucius"}
