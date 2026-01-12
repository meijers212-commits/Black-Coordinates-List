import requests
import json



class GetCoordinates:
    
    @staticmethod
    def ip_request(ip)-> json:
        try:
            if not ip:
                return "no ip reseived"
            url = f"http://ip-api.com/json/{ip}"
            data = requests.get(url).json()
            return data
        except Exception as Erorr:
            return Erorr
    
    @staticmethod
    def get_lat_lon(js)->list[dict]:
        try:
            if not js:
                return "no data reseived"
            data = []
            data.append({"lat":js["lat"]},{"lon":js["lon"]})
            return data
        except Exception as Erorr:
            return Erorr


