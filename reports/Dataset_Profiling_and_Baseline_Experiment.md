# Dataset Inspection and Refined Baseline Experiment

**Dataset:** Sephora `product_info.csv` supplied as a ZIP upload  
**Inspection date:** 12 November 2026

## Dataset profile

The CSV loaded with **8,494 rows and 27 columns**, including product names, brand, ingredients, prices in USD, ratings, highlights, and three category levels. There were 8,494 unique product IDs and no duplicate product IDs.

| Field | Missing rows |
|---|---:|
| Ingredients | 945 |
| Rating | 278 |
| Secondary category | 8 |
| Tertiary category | 990 |
| Highlights | 2,207 |

The primary category counts included 2,420 Skincare products, 2,369 Makeup products, 1,464 Hair products, and 1,432 Fragrance products. Price ranged from $3 to $1,900, with a median of $35. The average rating among 8,216 non-missing ratings was 4.19/5.

## Why the first baseline needed refinement

The initial broad Skincare category search returned an ingestible hydration gummy. This showed that primary category alone is not a sufficient product-type safeguard. A skincare discovery tool should avoid recommending supplements and wellness ingestibles as topical products.

## Refined baseline

The code now:
- Filters to the primary category `Skincare` by default.
- Excludes catalogue entries whose secondary category, tertiary category, or product name indicates wellness, supplements, or ingestibles (including gummies and vitamins).
- Supports product-type filtering and a maximum USD price.
- Uses TF-IDF and cosine similarity across product name, brand, category labels, highlights, and ingredients.
- Displays matching query terms as a lightweight explanation.

## Refined example experiment

Illustrative query: **“dry skin hydration hyaluronic acid moisturizer”**  
Budget: **up to USD 50**  
Catalogue filter: topical skincare, with the exclusions above.

| Product | Brand | Price (USD) | Similarity |
|---|---|---:|---:|
| Mini Plum Plump Hyaluronic Acid Moisturizer | Glow Recipe | 21.00 | 0.249 |
| FILLING GOOD hyaluronic acid plumping serum | Farmacy | 48.00 | 0.095 |
| Plum Plump Hyaluronic Acid Moisturizer | Glow Recipe | 39.00 | 0.095 |
| Omega+ Complex Moisturizer | Paula's Choice | 37.00 | 0.090 |
| Green Tea Hyaluronic Acid Hydrating Toner | Innisfree | 25.00 | 0.089 |

These are text-similarity results from the supplied catalogue, not evidence of clinical effectiveness, ingredient compatibility, or personalised safety. Scores are not probabilities.

## Interface and tests

A Streamlit interface is now included in `app.py`. It lets a user upload `product_info.csv`, enter a search phrase, set a maximum budget, choose a product type, and view a ranked shortlist. Basic automated tests cover exclusion of wellness ingestibles, product-type/budget filters, and the presence of explanations.

## Limitations and next steps

- This is a baseline content-matching prototype, not a clinically validated recommender.
- Ingredient text is missing for 945 rows and highlights for 2,207 rows.
- Category exclusions are a practical first safeguard and still require manual review.
- The current example query is illustrative; proper evaluation needs a documented set of test queries and relevance judgements.
- Similarity scores should not be interpreted as probabilities or medical suitability scores.
- Run the automated tests and the app in the target environment before public deployment.
