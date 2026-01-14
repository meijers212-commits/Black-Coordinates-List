import redis
import json
from schemas import PostIpAndCoordinates
class Connection:
    @staticmethod
    def get_connection():
        # שימוש בשם השירות מה-docker-compose
        return redis.Redis(host='database', port=6379, decode_responses=True)

class DBoperation:
    @staticmethod
    def insert_data_to_db(data: PostIpAndCoordinates) -> bool:
        try: 
            connection = Connection.get_connection()
            # שומר כ-String
            connection.set(data.ip, data.model_dump_json())
            return True
        except Exception:
            return False

    @staticmethod
    def get_all_from_db() -> list[dict]:
        connection = Connection.get_connection()
        all_keys = connection.keys()
        all_data = []
        for key in all_keys:
            raw_val = connection.get(key) 
            if raw_val:
                all_data.append({key: json.loads(raw_val)}) 
        return all_data