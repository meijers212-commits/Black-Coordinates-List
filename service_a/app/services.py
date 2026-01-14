import requests
import json
from pydantic import IPvAnyAddress 
from schemas import PostIpAndCoordinates



class GetCoordinates:

    @staticmethod
    def ip_request(ip: str):
        try:
            url = f"http://ip-api.com/json/{ip}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("status") == "fail":
                return None
            return data
        except Exception as e:
            print(f"IP Request Error: {e}")
            return None


    @staticmethod
    def get_lat_lon(json_data):
        if not json_data or "lat" not in json_data:
            return {"lat": "0", "lon": "0"}
        return {"lat": str(json_data["lat"]), "lon": str(json_data["lon"])}

    

 
    @staticmethod
    def connection_with_server_b(data: PostIpAndCoordinates): 
        try:
            url = "http://storage_api:5000/writ_to_db"
            
            payload = data.model_dump()
            payload["ip"] = str(payload["ip"])
            
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json() 
        except Exception as e:
            print(f"Error in Server A: {e}")
            raise e