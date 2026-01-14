from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI()

@app.post("/")
def foo():
    return { "hello": "world" }

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=5000)