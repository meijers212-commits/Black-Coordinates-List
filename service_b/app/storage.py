import redis 
from schemas import PostIpAndCoordinates,

class Connection:
    
    @staticmethod
    def get_connection():
        connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return connection


class DBopertion:

    @staticmethod
    def insert_data_to_db(data:PostIpAndCoordinates) -> bool:
        try: 
            connection = Connection.get_connection()
            connection.hset(data.ip,data.model_dump_json())
            connection.close()
            return True
        except Exception as error:
            return False
            

    @staticmethod
    def get_all_from_db() -> list[dict]:
        try:
            connection = Connection.get_connection()
            all_keys = connection.keys()
            all_data = []
            for key in all_keys:
                all_data.append({key:connection.hgetall(key)})
            connection.close()
            return all_data
        except Exception as error:
            raise error