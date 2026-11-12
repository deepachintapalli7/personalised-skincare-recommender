# Dataset Inspection and Baseline Experiment

**Dataset file:** `product_info.csv`  
**Source supplied by project owner:** ZIP uploaded for this project  
**Inspection date:** 12 November 2026

## 1. Dataset structure

The archive contained one CSV file, `product_info.csv`. It loaded successfully with **8,494 rows and 27 columns**. The dataset includes product identifiers and names, brand, ratings and review counts, ingredients, price in USD, product highlights, and three product-category levels.

The dataset contains **8,494 unique product IDs**; no duplicate product IDs were found in this inspection.

## 2. Missing-value inspection

| Field | Missing rows |
|---|---:|
| Product name | 0 |
| Brand name | 0 |
| Ingredients | 945 |
| Price (USD) | 0 |
| Rating | 278 |
| Primary category | 0 |
| Secondary category | 8 |
| Tertiary category | 990 |
| Highlights | 2,207 |

Ingredient and highlight text are incomplete for some products. The recommendation workflow should therefore treat missing text as unavailable information rather than assume the ingredient or product attribute is absent.

## 3. Category distribution

| Primary category | Products |
|---|---:|
| Skincare | 2,420 |
| Makeup | 2,369 |
| Hair | 1,464 |
| Fragrance | 1,432 |
| Bath & Body | 405 |
| Mini Size | 288 |
| Men | 60 |
| Tools & Brushes | 52 |
| Gifts | 4 |

Skincare represents 2,420 of the 8,494 catalogue rows. The initial recommender can filter to this category when testing skincare-specific searches.

## 4. Price and rating overview

The listed USD price had a mean of **$51.66**, median of **$35.00**, and range of **$3.00 to $1,900.00**. The upper end is much higher than the median, so price distributions should be inspected before using the mean as a typical-price description.

There were 8,216 non-missing ratings. The mean rating was **4.19** and the median was **4.29**, on the dataset's 1–5 rating scale. Ratings are not used as proof of product suitability.

## 5. Initial content-similarity experiment

A small baseline experiment was run on the 2,420 skincare rows. Product name, brand, category fields, highlights, and ingredient text were combined into a text representation. TF-IDF vectors and cosine similarity were used to rank matches for the illustrative query:

> dry skin hydration hyaluronic acid moisturizer

A maximum listed price of USD 50 was applied. The highest-ranked returned catalogue item was **Mini Plum Plump Hyaluronic Acid Moisturizer** (listed price and similarity score are retained in the experiment output / local analysis). Other high-ranked matches included hydration- and hyaluronic-acid-related products.

This is a demonstration of text matching, not a validated assessment of efficacy, safety, or personal compatibility. The result may include products that are not topical skincare (for example, ingestible products), so category and product-type filtering need refinement before presenting recommendations to users.

## 6. Changes made to the project code

The recommender now recognises the dataset's `price_usd` column, in addition to common price column names. This allows the budget filter to work with the supplied Sephora file. The raw CSV remains local and is not committed to the public GitHub repository.

## 7. Limitations and next steps

- Ingredient text is missing for 945 rows and highlights for 2,207 rows.
- Text similarity can surface semantically related but unsuitable products.
- The first experiment is not a user study and has no ground-truth relevance labels.
- Similarity scores are not probabilities or clinical suitability scores.
- Next, refine skincare-only product types, inspect candidate results, create test queries, and evaluate ranking quality using documented relevance judgements.
