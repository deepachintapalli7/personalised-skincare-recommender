# Week 4 — Exploratory Data Analysis and Feature Engineering

**Project:** Personalised Skincare Product Recommendation System

## Objective

Understand the structure and distribution of the product catalogue and identify features that may support relevant, explainable recommendations.

## Exploratory analysis plan

- Review dataset size, column types, unique product counts, and missing-value percentages.
- Examine product counts by category and brand where those fields exist.
- Inspect price distributions and identify unusual values that may reflect data-entry or currency-format issues.
- Review ingredient and description completeness.
- Compare available tags or attributes across product categories.
- Use charts only when they help reveal a pattern; label axes and explain what the chart does and does not show.

## Candidate features

| Feature | Potential use |
|---|---|
| Product category | Match the requested product type |
| Ingredient text | Compare ingredient-related preferences |
| Product description | Capture product purpose and characteristics |
| Price | Apply a stated budget range |
| Skin-type or concern tags | Match available catalogue tags, if present |
| Brand | Optional preference or display field |

Feature availability must be verified against the actual dataset. Missing fields must not be invented.

## Feature preparation ideas

Text fields may be combined selectively after cleaning. Ingredient names can be normalised carefully while preserving meaningful distinctions. Price should be converted to a consistent numeric representation after currency and unit checks. Categorical fields can be encoded if a later model requires it.

## Example analysis pattern

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/product_info.csv")
print(df.describe(include="all").T)
print(df.isna().mean().sort_values(ascending=False))

# Replace 'price' with the verified numeric price column.
# df["price"].dropna().plot(kind="hist", bins=20)
# plt.xlabel("Price")
# plt.ylabel("Number of products")
# plt.title("Product price distribution")
# plt.show()
```

## Status and limitations

This is the proposed EDA and feature-engineering workflow, not a report of completed statistical findings. Actual charts, distributions, and conclusions must be generated from the verified dataset and added with their observed values.
