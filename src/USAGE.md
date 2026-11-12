# Run SkinMatch locally

1. Install packages: `python -m pip install -r requirements.txt`
2. Put the permitted Sephora `product_info.csv` at `data/raw/product_info.csv`, or upload it in the app.
3. Start the interface: `streamlit run app.py`
4. Optional command line: `python -m src.recommender --data data/raw/product_info.csv --query "dry skin hyaluronic acid" --budget 50`
5. Run tests: `pytest -q`

The prototype filters to the Sephora Skincare primary category and excludes catalogue entries labelled Wellness, supplements, or ingestibles. Review results manually; this is a text-similarity demonstration, not medical advice.
