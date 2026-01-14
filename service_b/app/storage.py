import redis 
from schemas import PostIpAndCoordinates,PostRequests

class Connection:
    
    @staticmethod
    def get_connection():
        connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return connection


class DBopertion:

    @staticmethod
    def insert_data_to_db(data:PostIpAndCoordinates) -> PostRequests:
        try: 
            connection = Connection.get_connection()
            connection.hset(data.ip, mapping=data.coordinates)
            connection.close()
            requests = PostRequests(ip=data.ip,coordinates=data.coordinates,description="Content saved successfully to db.")
            return requests
        except Exception as error:
            requests = PostRequests(ip=data.ip,coordinates=data.coordinates,description=error)
            return requests
            

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
        
        