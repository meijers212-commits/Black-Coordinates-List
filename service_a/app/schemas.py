from pydantic import BaseModel ,Field,IPvAnyAddress


class PostIp(BaseModel):

    ip: IPvAnyAddress
    

