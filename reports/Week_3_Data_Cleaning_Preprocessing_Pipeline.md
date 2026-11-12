# Week 3 — Data Cleaning and Preprocessing Pipeline

**Project:** Personalised Skincare Product Recommendation System

## Objective

Prepare a reproducible process for checking and cleaning skincare product data before analysis. Product catalogues can contain missing descriptions, inconsistent category names, duplicated listings, mixed price formats, and ingredient text with inconsistent separators. These issues can affect similarity calculations and the quality of recommendations.

## Planned checks

1. Inspect dimensions, column names, data types, and sample records.
2. Measure missing values for important fields such as product name, category, price, description, and ingredients.
3. Identify exact and potential duplicate product records.
4. Standardise text fields by trimming whitespace and normalising case where appropriate.
5. Convert price fields to numeric values only after checking currency symbols and formatting.
6. Preserve unknown values rather than silently replacing them with misleading information.
7. Validate the cleaned output with row counts, type checks, and sample comparisons.

## Example implementation pattern

```python
import pandas as pd

df = pd.read_csv("data/raw/product_info.csv")
print(df.shape)
print(df.dtypes)
print(df.isna().sum().sort_values(ascending=False))

# Remove exact duplicate rows only after inspecting their meaning.
clean_df = df.drop_duplicates().copy()

for column in ["product_name", "brand", "category", "description"]:
    if column in clean_df.columns:
        clean_df[column] = clean_df[column].astype("string").str.strip()

print(clean_df.shape)
```

The column names above are examples and must be matched to the actual dataset schema before running the code.

## Quality and reproducibility

Keep the original raw file unchanged. Store cleaning logic in reusable code or a notebook, record every transformation, and compare before-and-after row counts. Do not remove records solely because one optional field is missing; decide based on the field's role in the recommendation workflow.

## Limitations and status

This document describes the planned pipeline and example code. No dataset-specific missing-value counts, removed-row totals, or cleaning outcomes are claimed until the code is run on the actual dataset.
