import requests
import json
from pydantic import IPvAnyAddress 
from schemas import PostIpAndCoordinates

class GetCoordinates:

    @staticmethod
    def ip_request(ip:IPvAnyAddress) -> json:
        try:
            if not ip:
                return {"Massege": "no ip reseived"}
            url = f"http://ip-api.com/json/{ip}"
            data = requests.get(url).json()
            return data
        except Exception as Erorr:
            return Erorr

    @staticmethod
    def get_lat_lon(json_data:json) -> dict[str,float]:
        try:
            if not json_data:
                return "no data reseived"
            data = {"lat": json_data["lat"], "lon": json_data["lon"]}
            return data
        except Exception as Erorr:
            return Erorr

    @staticmethod
    def conection_whit_server_b(data:PostIpAndCoordinates):
        url = 'https://localhost:8001/db_controler/post'
        x = requests.post(url, json = data.model_dump())
        return x.json()

        
