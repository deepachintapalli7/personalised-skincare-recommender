import pandas as pd
from src.recommender import load_products, recommend

def sample():
    return pd.DataFrame({
        "_product_name":["Hydrating Face Serum","Beauty Hydration Gummies","Clay Face Cleanser"],
        "_brand":["A","B","C"],
        "_primary":["Skincare","Skincare","Skincare"],
        "_secondary":["Treatments","Wellness","Cleansers"],
        "_tertiary":["Face Serums","Beauty Supplements","Face Wash & Cleansers"],
        "_search_text":["hyaluronic acid dry skin hydration serum","hyaluronic acid hydration gummies supplement","clay cleanser oily skin"],
        "_price":[25.0,20.0,15.0]
    })

def test_skincare_filter_excludes_ingestible_wellness():
    result=recommend(sample(),"hyaluronic acid hydration",budget=40)
    assert "Beauty Hydration Gummies" not in result["product"].tolist()

def test_product_type_and_budget_filters():
    result=recommend(sample(),"clay cleanser",budget=20,product_type="Cleansers")
    assert result["product"].tolist()==["Clay Face Cleanser"]

def test_recommendations_have_explanations():
    result=recommend(sample(),"hyaluronic acid dry skin")
    assert len(result)>0
    assert "matched_terms" in result.columns

def test_load_products_detects_non_first_alias(tmp_path):
    source = pd.DataFrame({
        "product_name": ["Hydrating Serum"],
        "brand_name": ["Example"],
        "primary_category": ["Skincare"],
        "secondary_category": ["Treatments"],
        "tertiary_category": ["Face Serums"],
        "highlights": ["Hydrating serum"],
        "ingredients": ["Hyaluronic Acid"],
        "price_usd": [25.0],
    })
    path = tmp_path / "catalogue.csv"
    source.to_csv(path, index=False)
    loaded, columns = load_products(path)
    assert columns["name"] == "product_name"
    assert columns["price"] == "price_usd"
    assert loaded.iloc[0]["_product_name"] == "Hydrating Serum"
