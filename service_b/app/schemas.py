from pydantic import BaseModel ,IPvAnyAddress
   
class PostIp(BaseModel):
    ip: str
   
class PostIpAndCoordinates(PostIp):
    lat: str
    lon: str