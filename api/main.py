from fastapi import FastAPI

from api.schemas import (
    QueryRequest,
    RecommendationResponse,
    ProductResponse
)

from api.recommender_api import get_recommendations


# --------------------------------
# Create FastAPI App
# --------------------------------

app = FastAPI(

    title="AI Electronics Recommendation API",

    description="FastAPI for AI Electronics Accessories Recommendation System",

    version="1.0.0"

)


# --------------------------------
# Home Route
# --------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Electronics Recommendation API is Running Successfully!"
    }


# --------------------------------
# Recommendation Route
# --------------------------------

@app.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend(request: QueryRequest):

    recommendations = get_recommendations(request.query)

    products = []

    for item in recommendations:

        products.append(

            ProductResponse(

                name=item["name"],

                price=item["price"],

                rating=item["rating"],

                similarity=item["similarity"],

                image_name=item["image_name"],

                link=item["link"]

            )

        )

    return RecommendationResponse(

        query=request.query,

        recommendations=products

    )