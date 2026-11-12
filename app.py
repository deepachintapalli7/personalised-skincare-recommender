import streamlit as st
import pandas as pd
from src.recommender import load_products, recommend

st.set_page_config(page_title="SkinMatch | Skincare Finder",page_icon="🧴",layout="wide")
st.title("SkinMatch")
st.caption("A transparent skincare product discovery prototype powered by the Sephora catalogue.")
st.info("For product discovery only—not medical advice. Similarity does not establish safety, compatibility, or effectiveness.")
uploaded=st.file_uploader("Upload Sephora product_info.csv",type=["csv"])
local_path=st.text_input("Or enter the local CSV path",value="data/raw/product_info.csv")
@st.cache_data(show_spinner=False)
def read_data(file_bytes):
    import io
    import tempfile, os
    with tempfile.NamedTemporaryFile(suffix=".csv",delete=False) as f:
        f.write(file_bytes); path=f.name
    try: return load_products(path)[0]
    finally: os.unlink(path)
products=None
try:
    if uploaded: products=read_data(uploaded.getvalue())
    else:
        import os
        if os.path.exists(local_path): products=load_products(local_path)[0]
except Exception as e:
    st.error(f"Could not read dataset: {e}")
if products is not None:
    st.success(f"Loaded {len(products):,} product records.")
    left,right=st.columns(2)
    with left:
        concern=st.text_input("What are you looking for?",placeholder="e.g. dry skin hyaluronic acid hydration")
        max_price=st.number_input("Maximum budget (USD)",min_value=0.0,value=50.0,step=5.0)
    with right:
        types=sorted(set(products.loc[products["_primary"].str.casefold().eq("skincare"),"_secondary"].dropna())-{"Wellness"})
        selected=st.selectbox("Product type",["Any topical skincare type"]+types)
        count=st.slider("Number of recommendations",3,15,5)
    if st.button("Find matching products",type="primary"):
        if not concern.strip(): st.warning("Enter a concern or product preference first.")
        else:
            ptype=None if selected=="Any topical skincare type" else selected
            try:
                results=recommend(products,concern,budget=max_price,product_type=ptype,top_n=count)
                if results.empty: st.warning("No matches. Try a broader search or a higher budget.")
                else:
                    st.subheader("Your product shortlist")
                    st.dataframe(results.rename(columns={"product":"Product","brand":"Brand","price_usd":"Price (USD)","similarity":"Text similarity","matched_terms":"Matching terms"}),use_container_width=True,hide_index=True)
                    st.caption("Similarity is a text-ranking score, not a probability or clinical suitability score.")
            except Exception as e: st.error(str(e))
else:
    st.warning("Upload product_info.csv or place it at data/raw/product_info.csv to start.")
