from fastapi import APIRouter
from schemas import PostIpAndCoordinates, PostRequests



redis_conactor_server = APIRouter()


@redis_conactor_server.post("/writ_to_db")
def save_to_data_base():
    pass
   
 
@redis_conactor_server.get("/get_all")
def get_all_from_db():
    pass


