# Running the baseline recommender

## 1. Install dependencies

From the repository root:

```bash
python -m pip install -r requirements.txt
```

## 2. Keep your dataset local

Place your permitted product CSV at `data/raw/product_info.csv`. Raw data is ignored by Git and should not be pushed to this public repository.

## 3. Run a recommendation

```bash
python -m src.recommender --data data/raw/product_info.csv --query "dry skin hyaluronic acid moisturizer" --budget 30 --top 5
```

Optional category filter:

```bash
python -m src.recommender --data data/raw/product_info.csv --query "fragrance free hydration" --category "Moisturizers" --top 5
```

The budget uses the same currency and units as the dataset. Omit `--budget` if you do not want a price filter.

## What this baseline does

- Detects common product, brand, category, description, ingredient, and price columns.
- Cleans blank product names and exact duplicate product/text pairs.
- Builds TF-IDF text vectors and ranks catalogue entries by cosine similarity.
- Applies optional category and maximum-price filters.
- Displays query-term overlap as a lightweight explanation.

## Important limitations

This is an initial text-similarity baseline. Similarity is not proof of ingredient compatibility, safety, or clinical effectiveness. It does not diagnose skin conditions or guarantee results. Column detection depends on the actual CSV schema; review the detected columns before interpreting results. Evaluation metrics and model performance have not yet been measured.
