from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class ProductResponse(BaseModel):
    name: str
    price: str
    rating: str
    similarity: float
    image_name: str
    link: str


class RecommendationResponse(BaseModel):
    query: str
    recommendations: list[ProductResponse]