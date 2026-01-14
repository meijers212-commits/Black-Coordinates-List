from fastapi import FastAPI
import uvicorn
from routes import redis_conactor_server

app = FastAPI()

app.include_router(redis_conactor_server, tags=["db_controler"])

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8001)