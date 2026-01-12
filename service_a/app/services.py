import requests
import json


class GetCoordinates:

    @staticmethod
    def ip_request(ip) -> json:
        try:
            if not ip:
                return "no ip reseived"
            url = f"http://ip-api.com/json/{ip}"
            data = requests.get(url).json()
            return data
        except Exception as Erorr:
            return Erorr

    @staticmethod
    def get_lat_lon(json_data) -> list[dict]:
        try:
            if not json_data:
                return "no data reseived"
            data = [{"lat": json_data["lat"]}, {"lon": json_data["lon"]}]
            return data
        except Exception as Erorr:
            return Erorr
