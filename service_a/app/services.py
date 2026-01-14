import requests
import json
from pydantic import IPvAnyAddress 
from schemas import PostIpAndCoordinates
import os

SERVICE_B_HOST = os.getenv("SERVICE_B_HOST", "localhost")
SERVICE_B_PORT = os.getenv("SERVICE_B_PORT", "5000") 

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
    def connection_with_server_b(data_to_send):
        # בניית הכתובת בצורה דינמית
        url = f"http://{SERVICE_B_HOST}:{SERVICE_B_PORT}/save_coordinates"
        
        try:
            response = requests.post(url, json=data_to_send)
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}
        