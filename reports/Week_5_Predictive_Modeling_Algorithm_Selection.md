# Week 5 — Predictive Modeling and Algorithm Selection

**Project:** Personalised Skincare Product Recommendation System

## Problem framing

The project is a product discovery and ranking task. The initial goal is to recommend catalogue items based on product attributes and a user's stated needs, rather than predict a medical outcome.

## Candidate approach: content-based filtering

A content-based baseline is appropriate when reliable user-rating or transaction history is unavailable. It compares product representations using fields such as category, ingredient text, and descriptions.

A possible baseline workflow:

1. Select and clean relevant text fields.
2. Convert text into numerical vectors using TF-IDF.
3. Represent the user's stated preferences as a query or selected feature profile.
4. Calculate cosine similarity between the query representation and product representations.
5. Apply explicit product-type and budget filters where data permits.
6. Return a ranked shortlist with matching attributes and limitations.

## Why this baseline

TF-IDF and cosine similarity are interpretable starting points for text-based similarity and do not require a large labelled training dataset. They can support a useful baseline while keeping the method relatively simple for a first implementation.

## Alternatives and trade-offs

- **Collaborative filtering:** may be useful if sufficient user-item interaction data becomes available; it is not appropriate to assume such data exists.
- **Clustering (for example, K-Means):** may help explore groups of similar products but does not by itself provide a personalised ranked recommendation.
- **Decision trees:** require a suitable target label and should not be used to predict suitability without defensible labels.

## Evaluation plan

Evaluation should use a documented test set or carefully designed test cases. Possible measures include Precision@K, Recall@K, ranking quality, catalogue coverage, and qualitative checks of whether the returned products satisfy explicit constraints. The choice of metric depends on the available ground truth.

## Responsible-use limits

Similarity is not proof of ingredient compatibility or clinical effectiveness. The system should not diagnose conditions, guarantee results, or make unsupported safety claims.

## Status

This report selects a proposed baseline and evaluation plan. It does not claim that a model has been trained, that recommendations have been generated, or that performance metrics have been measured.
