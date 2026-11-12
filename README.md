# Personalised Skincare Product Recommender

An explainable data science project exploring how skincare product information can support personalised product discovery.

## Project goal

The project aims to help users compare skincare products using their selected skin concerns, product categories, ingredients, and budget. The intended recommendation approach is content-based filtering, with clear explanations of why a product is suggested.

## Project status

This repository is being developed as part of a YuvaIntern data science internship in the Beauty & Wellness domain.

- Weeks 1–2: internship reports prepared; the Week 2 report is available in `reports/`.
- Weeks 3–6: planning and methodology reports prepared. These are not evidence of completed model training or measured evaluation results.
- The Sephora catalogue was profiled locally (8,494 source rows; 8,482 retained after empty-name and duplicate removal). The baseline recommender and four automated tests have been run successfully against the project logic and a local catalogue copy. This is an initial text-similarity prototype, not a clinically validated recommendation model.

## Repository structure

- `data/` — dataset documentation; raw datasets are kept locally and are not committed.
- `notebooks/` — analysis notebooks.
- `reports/` — weekly internship reports.
- `src/` — reusable project source code.
- `requirements.txt` — Python dependencies.

## Initial implementation

A Streamlit interface is available in `app.py`. Run it with `streamlit run app.py`, then upload the local `product_info.csv` file in the app. The baseline filters the catalogue to skincare and excludes common wellness/ingestible listings, with optional product-type and budget filters.

An initial content-based recommendation baseline is available in `src/recommender.py`. It uses TF-IDF and cosine similarity, with optional budget and category filters. See [src/USAGE.md](src/USAGE.md) for setup and commands. Basic tests are in `tests/`.

The baseline was checked against the uploaded Sephora catalogue. Its similarity score is a text-ranking signal only; it does not measure product safety, compatibility, or clinical effectiveness.

## Planned workflow

1. Inspect and understand the product dataset.
2. Clean relevant product fields and ingredient information.
3. Perform exploratory data analysis.
4. Engineer useful product features.
5. Build a content-based recommendation baseline.
6. Evaluate recommendations with suitable ranking and coverage metrics once valid test data is available.

## Setup

Use Python 3.10 or later.

```bash
python -m pip install -r requirements.txt
```

## Deploy the app

The app is configured for Streamlit Community Cloud. To publish it, sign in at [share.streamlit.io](https://share.streamlit.io/) with the GitHub account that owns this repository, choose **Create app**, then select:
- Repository: `deepachintapalli7/personalised-skincare-recommender`
- Branch: `main`
- Main file path: `app.py`

Deploy the app, then upload the `product_info.csv` dataset in the app itself. The raw dataset is intentionally not stored in this public repository. See the [official Streamlit deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## Data and responsible use

Do not commit large raw datasets, personal data, or credentials. Check product ingredients and claims against reliable sources; recommendations are for product discovery and are not medical advice.

## Current limitations

No recommendation model performance or business impact is claimed until it has been measured on an appropriate dataset and documented with reproducible results.
