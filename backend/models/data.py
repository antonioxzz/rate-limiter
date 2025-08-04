from pydantic import BaseModel, Field

class DataResponse(BaseModel):
    message: str = Field(..., example="This is protected data.")
    client_ip: str = Field(..., example="127.0.0.1")

    class Config:
        from_attributes = True
