from fastapi import APIRouter
from schemas import PostIp, PostIpAndCoordinates
from services import GetCoordinates 
import requests

router = APIRouter()



@router.get("/health")
def health_check():
    return {"status": "ok"}



@router.post("/ip")
def client_api_manegment(ip: PostIp):
   
    raw_data = GetCoordinates.ip_request(ip.ip)

    if raw_data is None:
        return {"error": "Could not resolve IP address"}
   
    coordinates = GetCoordinates.get_lat_lon(raw_data)
    
    data_to_send = PostIpAndCoordinates(
        ip=ip.ip, 
        lat=coordinates["lat"], 
        lon=coordinates["lon"]
    )
  
    return GetCoordinates.connection_with_server_b(data_to_send)