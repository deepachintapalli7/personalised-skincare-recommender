# Week 1 — Data Science Orientation and Problem Definition

**Internship domain:** Beauty & Wellness  
**Project:** Personalised Skincare Product Recommendation System  
**Intern:** Deepa Chintapalli

## 1. Industry context

Beauty and wellness customers face a large and frequently changing choice of skincare products. Products differ by purpose, formulation, ingredients, skin-type suitability, size, and price. Product descriptions can also contain technical ingredient names that are difficult for a new customer to interpret. As a result, selecting a product can require comparing many listings and reading multiple ingredient descriptions.

Data science can support this decision by organising product information into searchable features and helping customers discover products that match stated preferences. A recommendation system should assist comparison rather than make medical claims or guarantee that a product will work for every person.

## 2. Selected business problem

The selected problem is **difficulty finding skincare products that align with a customer's skin concern, ingredient preferences, product type, and budget**.

A customer may want a moisturiser for dry skin, prefer products without a particular ingredient, and have a limited budget. A basic product catalogue search may return many products but may not explain which options best match all these requirements. The project will explore a transparent recommendation approach that ranks products using available product attributes.

## 3. Why this problem matters

A well-designed discovery tool can reduce the effort involved in comparing products, make catalogue information easier to understand, and provide a more consistent way to shortlist options. For a business, relevant product discovery may improve the customer experience and help users explore products that fit their needs. These are potential benefits to be evaluated; no business impact is claimed at this planning stage.

## 4. Research questions

1. Which product fields are available and sufficiently complete for recommendation?
2. Can product category, description, ingredients, and price be converted into useful features?
3. Can a content-based method rank products that share relevant attributes with a customer's stated needs?
4. How can recommendations explain the attributes that caused a product to be suggested?
5. What limitations arise from missing ingredient data, incomplete product descriptions, or subjective skin concerns?

## 5. Initial hypotheses

- Product category, ingredient text, and product description may provide useful signals for content-based similarity.
- Including a budget constraint may make the shortlist more practically relevant.
- Showing matching attributes alongside each suggestion may make recommendations easier to understand.
- Incomplete or inconsistent product data may reduce recommendation quality.

These are hypotheses to test, not findings.

## 6. Proposed data science approach

The planned workflow is to identify a suitable public product dataset, inspect its schema, document its source and permitted use, clean relevant fields, and conduct exploratory data analysis. Candidate features include product type, ingredient text, product description, price, and any available skin-type or concern tags. A content-based baseline using text vectorisation and cosine similarity is a reasonable starting point because it can compare product descriptions without requiring user-rating history.

The system should apply clear filters for user constraints where possible and display concise explanations of matches. Evaluation will require a documented test strategy and suitable ranking measures. Actual metrics will only be reported after implementation and testing.

## 7. Responsible-use considerations

Skincare recommendations are not medical advice. Ingredient suitability can depend on concentration, formulation, allergies, and individual circumstances that may not be represented in a dataset. The system should avoid diagnosing skin conditions, avoid unsupported safety claims, and clearly communicate data limitations. Dataset licensing and redistribution conditions must be checked before sharing data.

## 8. Current status and next steps

This report defines the business problem, research questions, hypotheses, and proposed workflow. It does not claim that a dataset has been analysed or that a recommendation model has been trained. The next step is to inspect the selected dataset, verify its columns and data quality, and record evidence from actual analysis.
