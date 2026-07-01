from pydantic import BaseModel, HttpUrl


class ConvertRequest(BaseModel):
    url: HttpUrl