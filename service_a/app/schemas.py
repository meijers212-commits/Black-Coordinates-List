from pydantic import BaseModel ,Field,IPvAnyAddress


class PostIp(BaseModel):
    ip: IPvAnyAddress
    
class PostIpAndCoordinates(BaseModel):
    ip :IPvAnyAddress
    coordinates : dict[str,float]

