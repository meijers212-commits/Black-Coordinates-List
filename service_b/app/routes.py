from fastapi import APIRouter
from schemas import PostIpAndCoordinates, PostRequests
from storage import DBopertion as DB


redis_conactor_server = APIRouter()


@redis_conactor_server.post("/writ_to_db")
def save_to_data_base(data:PostIpAndCoordinates):
    requests = DB.insert_data_to_db(data)
    return requests
 
@redis_conactor_server.get("/get_all")
def get_all_from_db():
    pass


