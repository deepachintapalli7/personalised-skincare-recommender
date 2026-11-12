import pandas as pd

from src.recommender import recommend


def test_recommend_returns_matching_product():
    products = pd.DataFrame({
        "_product_name": ["Hydrating Serum", "Clay Cleanser"],
        "_search_text": [
            "hyaluronic acid hydration dry skin serum",
            "clay cleanser oily skin",
        ],
        "_category": ["Serums", "Cleansers"],
        "_price": [20.0, 12.0],
    })
    result = recommend(products, "hyaluronic acid dry skin", top_n=1)
    assert result.iloc[0]["product"] == "Hydrating Serum"


def test_budget_filter_excludes_expensive_product():
    products = pd.DataFrame({
        "_product_name": ["Budget Moisturizer", "Premium Moisturizer"],
        "_search_text": ["glycerin moisturizer hydration", "glycerin moisturizer hydration"],
        "_category": ["Moisturizers", "Moisturizers"],
        "_price": [10.0, 80.0],
    })
    result = recommend(products, "glycerin hydration", budget=20)
    assert result["product"].tolist() == ["Budget Moisturizer"]
