from fastapi import APIRouter
from schemas import PostIpAndCoordinates
from storage import DBopertion as DB


router = APIRouter()

@router.post("/writ_to_db")
def save_to_data_base(data: PostIpAndCoordinates):
    requests = DB.insert_data_to_db(data)
    return requests
 
@router.get("/get_all")
def get_all_from_db():
    return DB.get_all_from_db()
    

