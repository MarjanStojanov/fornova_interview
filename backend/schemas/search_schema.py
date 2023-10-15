from pydantic import BaseModel, Field


class SearchSchema(BaseModel):
    page: int = Field(gt=0)
    limit: int = Field(gt=0)
    keyword: str = Field(min_length=3)
