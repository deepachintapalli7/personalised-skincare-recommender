"""Explainable content-based skincare product recommender.

This is a baseline for product discovery, not medical advice. It ranks
catalogue items from text attributes and applies optional budget/category filters.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


COLUMN_ALIASES = {
    "name": ["product_name", "product", "name", "product_title"],
    "brand": ["brand_name", "brand"],
    "category": ["primary_category", "secondary_category", "tertiary_category",
                 "category", "product_type"],
    "description": ["description", "details", "highlights", "about"],
    "ingredients": ["ingredients", "ingredient_list", "ingredient"],
    "price": ["price", "sale_price", "current_price"],
}


def _find_columns(frame: pd.DataFrame) -> dict[str, list[str]]:
    normalised = {str(c).strip().lower(): c for c in frame.columns}
    found: dict[str, list[str]] = {}
    for role, aliases in COLUMN_ALIASES.items():
        matches = [normalised[a] for a in aliases if a in normalised]
        if matches:
            found[role] = matches
    return found


def _clean_text(value: object) -> str:
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def load_products(csv_path: str | Path) -> tuple[pd.DataFrame, dict[str, list[str]]]:
    """Load a local product CSV and create a clean, combined text field."""
    frame = pd.read_csv(csv_path)
    columns = _find_columns(frame)
    if not columns.get("name"):
        raise ValueError(
            "Could not identify a product-name column. Expected one of: "
            + ", ".join(COLUMN_ALIASES["name"])
        )

    result = frame.copy()
    for role, cols in columns.items():
        if role != "price":
            result[f"_{role}"] = result[cols].fillna("").astype(str).agg(" ".join, axis=1).map(_clean_text)

    result["_product_name"] = result[columns["name"][0]].map(_clean_text)
    text_fields = [c for c in ["_product_name", "_category", "_description", "_ingredients", "_brand"] if c in result]
    result["_search_text"] = result[text_fields].agg(" ".join, axis=1).map(_clean_text)

    price_col = columns.get("price", [None])[0]
    if price_col:
        result["_price"] = pd.to_numeric(
            result[price_col].astype(str).str.replace(r"[^0-9.]", "", regex=True),
            errors="coerce",
        )
    else:
        result["_price"] = float("nan")

    result = result[result["_product_name"].ne("")].drop_duplicates(
        subset=["_product_name", "_search_text"]
    ).reset_index(drop=True)
    if result.empty:
        raise ValueError("No usable product rows found after basic cleaning.")
    return result, columns


def recommend(
    products: pd.DataFrame,
    query: str,
    budget: float | None = None,
    category: str | None = None,
    top_n: int = 10,
) -> pd.DataFrame:
    """Rank products by text similarity and return simple match explanations."""
    if not query.strip():
        raise ValueError("Enter a skin concern, ingredient preference, or product need.")
    if top_n < 1:
        raise ValueError("top_n must be at least 1.")

    candidates = products.copy()
    if budget is not None:
        if "_price" not in candidates or candidates["_price"].notna().sum() == 0:
            raise ValueError("A usable price column was not found, so budget filtering is unavailable.")
        candidates = candidates[candidates["_price"].le(budget)]
    if category:
        if "_category" not in candidates:
            raise ValueError("A product category column was not found.")
        candidates = candidates[candidates["_category"].str.contains(
            re.escape(category), case=False, na=False
        )]
    if candidates.empty:
        return pd.DataFrame(columns=["product", "price", "similarity", "matched_terms"])

    corpus = candidates["_search_text"].fillna("").tolist()
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(corpus + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
    terms = set(re.findall(r"[a-zA-Z][a-zA-Z0-9-]+", query.lower()))

    candidates = candidates.copy()
    candidates["_score"] = scores
    candidates = candidates.sort_values("_score", ascending=False).head(top_n)

    def explanation(text: str) -> str:
        words = set(re.findall(r"[a-zA-Z][a-zA-Z0-9-]+", text.lower()))
        return ", ".join(sorted(terms & words)) or "overall text similarity"

    output = pd.DataFrame({
        "product": candidates["_product_name"],
        "price": candidates["_price"],
        "similarity": candidates["_score"].round(3),
        "matched_terms": candidates["_search_text"].map(explanation),
    })
    return output.reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Find skincare products by catalogue text.")
    parser.add_argument("--data", required=True, help="Path to local product CSV")
    parser.add_argument("--query", required=True, help="Concern, ingredient preference, or product need")
    parser.add_argument("--budget", type=float, default=None, help="Maximum price in dataset currency")
    parser.add_argument("--category", default=None, help="Optional category filter")
    parser.add_argument("--top", type=int, default=10, help="Number of recommendations")
    args = parser.parse_args()

    products, columns = load_products(args.data)
    print(f"Loaded {len(products)} products.")
    print(f"Detected columns: {columns}")
    results = recommend(products, args.query, args.budget, args.category, args.top)
    if results.empty:
        print("No products matched those filters. Try a broader query or budget.")
    else:
        print(results.to_string(index=False))


if __name__ == "__main__":
    main()
