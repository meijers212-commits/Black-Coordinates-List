from fastapi import APIRouter
from schemas import PostIp
from services import GetCoordinates as gc



ip_router = APIRouter()


@ip_router.post("/ip")
def client_api_manegment(ip:PostIp):
    coordinates = gc.get_lat_lon(gc.ip_request(ip.ip))
    return coordinates

        


