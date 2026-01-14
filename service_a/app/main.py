from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI()

app.include_router(router, tags=["ip-coordinates"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)