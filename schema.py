from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

class BlogShow(Blog):
    class Config:
        from_attributes = True
