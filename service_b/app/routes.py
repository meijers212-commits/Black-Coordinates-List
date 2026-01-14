from fastapi import APIRouter
from schemas import PostIpAndCoordinates
from storage import DBoperation as DB


router = APIRouter()


@router.post("/writ_to_db")
def save_to_data_base(data: PostIpAndCoordinates):
    try:
        success = DB.insert_data_to_db(data)
        return {"status": "success", "saved": success} # להחזיר JSON תקין
    except Exception as e:
        print(f"Error in Server B: {e}")
        return {"status": "error", "message": str(e)}



@router.get("/get_all")
def get_all_from_db():
    return DB.get_all_from_db()
    

