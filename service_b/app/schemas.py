from pydantic import BaseModel ,IPvAnyAddress
   
class PostIp(BaseModel):
    ip: IPvAnyAddress
   
class PostIpAndCoordinates(PostIp):
    lat: str
    lon: str