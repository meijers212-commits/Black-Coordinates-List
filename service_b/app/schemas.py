from pydantic import BaseModel ,IPvAnyAddress
from typing import Optional
   
class PostIp(BaseModel):
    ip: IPvAnyAddress
   
class PostIpAndCoordinates(PostIp):
    lat: str
    lon: str