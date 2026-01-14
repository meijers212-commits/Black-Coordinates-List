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
    def get_lat_lon(json_data:json) :
        try:
            if not json_data:
                return "no data reseived"
            data = {"lat": str(json_data["lat"]), "lon": str(json_data["lon"])}
            return data
        except Exception as Erorr:
            return Erorr

    @staticmethod
    def conection_whit_server_b(data:PostIpAndCoordinates):
        try:
            url = "http://localhost:5000/writ_to_db"
            dataa = data.model_dump_json()
            requests.post(url, dataa)
            # return True
        except Exception as e:
            # raise e
            print(e)

        
