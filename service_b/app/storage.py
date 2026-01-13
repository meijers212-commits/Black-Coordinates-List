import redis 
import json

class Connection:
    
    @staticmethod
    def get_connection():
        connection = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return connection


class DBopertion:

    @staticmethod
    def insert_data_to_db(data):
        try: 
            connection = Connection.get_connection()
            connection.set(data.ip,json.dumps(data.coordinates))
            connection.close()
            data.description = "Content saved successfully to db."
            return data.description
        except Exception as e:
            raise e 

    @staticmethod
    def get_all_from_db():
        try:
            connection = Connection.get_connection()
            all_keys = connection.keys()
            all_data = []
            for key in all_keys:
                all_data.append({key:connection.get(key)})
            connection.close()
            return all_data
        except Exception as e:
            raise e 