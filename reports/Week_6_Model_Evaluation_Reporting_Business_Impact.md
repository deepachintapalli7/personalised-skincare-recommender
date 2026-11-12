# Week 6 — Model Evaluation, Reporting, and Business Impact

**Project:** Personalised Skincare Product Recommendation System

## Objective

Define how the recommendation approach should be evaluated and communicated responsibly once implementation and testing are complete.

## Evaluation dimensions

**Relevance:** Do the top-ranked products match the user's requested product type and available preference fields?

**Ranking quality:** Are the most relevant items placed near the top? Precision@K and Recall@K may be used if reliable relevance labels or test judgements are available.

**Coverage:** Does the system recommend a reasonable range of catalogue items, or does it repeatedly return only a small group?

**Constraint satisfaction:** Do results respect explicit filters such as budget and product category when the required data is available?

**Explainability:** Can the system show which product attributes contributed to a recommendation?

## Testing strategy

Create representative test cases covering different product types, concerns, ingredient preferences, and budgets. Keep test cases separate from any data used to tune the method. Review failure cases, including missing ingredient information, ambiguous user requests, and products with incomplete descriptions. Record the dataset version, preprocessing steps, model settings, and evaluation date so results can be reproduced.

## Reporting template

| Measure | Result |
|---|---|
| Precision@K | To be measured |
| Recall@K | To be measured |
| Catalogue coverage | To be measured |
| Constraint satisfaction | To be measured |
| Test cases reviewed | To be recorded |

Do not fill these fields with invented scores. Explain the test data and calculation method alongside every reported result.

## Potential business value

A successful product discovery tool could reduce comparison effort, improve the clarity of product exploration, and help customers shortlist products aligned with stated preferences. These are potential outcomes, not proven impacts. Business impact would require user testing and appropriate evidence, such as task completion time, satisfaction feedback, or conversion analysis conducted with permission.

## Limitations and ethical considerations

The available dataset may be incomplete, outdated, or inconsistent. Ingredient lists alone cannot establish whether a product is safe or suitable for an individual. The system must avoid medical diagnosis and unsupported efficacy claims. User information should be minimised and protected.

## Conclusion and status

This report defines an evaluation and communication framework. No measured model performance or business impact is claimed until implementation, testing, and evidence collection are complete.
