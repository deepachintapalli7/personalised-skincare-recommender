"""Explainable content-based skincare product recommender."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ALIASES = {
    "name": ["product_name", "product", "name", "product_title"],
    "brand": ["brand_name", "brand"],
    "primary": ["primary_category"],
    "secondary": ["secondary_category"],
    "tertiary": ["tertiary_category"],
    "description": ["description", "details", "highlights", "about"],
    "ingredients": ["ingredients", "ingredient_list", "ingredient"],
    "price": ["price_usd", "price", "sale_price_usd", "sale_price", "current_price"],
}
EXCLUDED_TERMS = ("supplement", "wellness", "ingestible", "gummy", "vitamin")

def _clean(value):
    if pd.isna(value): return ""
    return re.sub(r"\s+", " ", str(value)).strip()

def load_products(csv_path: str | Path):
    frame = pd.read_csv(csv_path, low_memory=False)
    lookup = {str(c).strip().lower(): c for c in frame.columns}
    cols = {k: lookup[v[0]] for k,v in ALIASES.items() if any(x in lookup for x in v)}
    for k, aliases in ALIASES.items():
        if k not in cols:
            cols[k] = next((lookup[x] for x in aliases if x in lookup), None)
    if cols["name"] is None: raise ValueError("Product-name column not found.")
    out = frame.copy()
    for key in ("brand","primary","secondary","tertiary","description","ingredients"):
        c=cols.get(key)
        out["_"+key] = out[c].map(_clean) if c else ""
    out["_product_name"] = out[cols["name"]].map(_clean)
    out["_price"] = pd.to_numeric(out[cols["price"]], errors="coerce") if cols.get("price") else float("nan")
    out["_search_text"] = out[["_product_name","_brand","_primary","_secondary","_tertiary","_description","_ingredients"]].agg(" ".join,axis=1).map(_clean)
    out=out[out["_product_name"].ne("")].drop_duplicates(subset=["_product_name","_search_text"]).reset_index(drop=True)
    return out, cols

def recommend(products, query, budget=None, product_type=None, top_n=10, skincare_only=True):
    if not query.strip(): raise ValueError("Enter a product need or ingredient preference.")
    if top_n < 1: raise ValueError("top_n must be positive.")
    c=products.copy()
    if skincare_only and "_primary" in c:
        c=c[c["_primary"].str.casefold().eq("skincare")]
        combined=(c["_secondary"]+" "+c["_tertiary"]+" "+c["_product_name"]).str.casefold()
        excluded="|".join(map(re.escape,EXCLUDED_TERMS))
        c=c[~combined.str.contains(excluded,na=False)]
    if product_type:
        combined=(c["_secondary"]+" "+c["_tertiary"]).str.casefold()
        c=c[combined.str.contains(re.escape(product_type.casefold()),na=False)]
    if budget is not None:
        if c["_price"].notna().sum()==0: raise ValueError("No usable price data for budget filtering.")
        c=c[c["_price"].le(budget)]
    if c.empty: return pd.DataFrame(columns=["product","brand","price_usd","similarity","matched_terms"])
    vec=TfidfVectorizer(stop_words="english",ngram_range=(1,2))
    matrix=vec.fit_transform(c["_search_text"].fillna("").tolist()+[query])
    scores=cosine_similarity(matrix[-1],matrix[:-1]).ravel()
    qterms=set(re.findall(r"[a-zA-Z][a-zA-Z0-9-]+",query.casefold()))
    c=c.copy(); c["_score"]=scores
    c=c.sort_values(["_score","_price"],ascending=[False,True]).head(top_n)
    def matches(text):
        terms=set(re.findall(r"[a-zA-Z][a-zA-Z0-9-]+",text.casefold()))
        return ", ".join(sorted(qterms & terms)) or "overall text similarity"
    return pd.DataFrame({
        "product":c["_product_name"],"brand":c["_brand"],"price_usd":c["_price"],
        "similarity":c["_score"].round(3),"matched_terms":c["_search_text"].map(matches)
    }).reset_index(drop=True)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",required=True); p.add_argument("--query",required=True)
    p.add_argument("--budget",type=float); p.add_argument("--type",dest="product_type")
    p.add_argument("--top",type=int,default=10)
    a=p.parse_args(); products,cols=load_products(a.data)
    print(f"Loaded {len(products)} catalogue rows. Detected: {cols}")
    print(recommend(products,a.query,a.budget,a.product_type,a.top).to_string(index=False))
if __name__=="__main__": main()
