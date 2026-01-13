from fastapi import FastAPI, APIRouter, HTTPException
from schemas import PostIp




router = APIRouter()


@router.post("/ip")
def client_api_manegment(ip:PostIp):
    
    
        


