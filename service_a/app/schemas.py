from pydantic import BaseModel ,IPvAnyAddress
from typing import Optional

class PostIp(BaseModel):
    ip: IPvAnyAddress
    
class PostIpAndCoordinates(BaseModel):
    ip :IPvAnyAddress
    coordinates : dict[str,float]

class GetRequests(BaseModel):
    ip :IPvAnyAddress
    coordinates : dict[str,float]
    description: Optional[str] = None