# Predicting Medical Proffessionals From OkCupid Profile Data

## Problem Statement
Presented with a dataset of self reported characteristics of users taken from a dating site, can we build a binary classifier model that will predict who works in the medical profession?

## Data
The dataset used is the OkCupid Dataset available [here](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles).

The dataset consists of self-reported demographic and behavioural attributes taken from an online dating platform.

Size of the dataset is 31 attributes with 59,946 entries.

2 attributes are numerical, 10 are unstructured data, 1 is date-time, 1 is geospatial, 17 are categorical/ordincal.

It is important to note that this dataset does not include any identifying characteristics.

## Methodology

### Performance Measure
As the problem is a classification problem, the performance measures chosen are:
1. Confusion Matrix
2. Reciver Operating Characteristic (ROC) Curve - Area under the curve (AUC)

Accuracy is not used as the primary metric due to the skewed class distribution.

### Assumptions
1. The train/test split method is representative and will produces two subsets drawn from the underlying distribution.
2. Observations are independent and each row represents an independent individual.
3. The labels in the dataset are reliable.
4. The preprocessing correctly encodes and preserves the  feature semantics of the original variables.


## Results
Stochastic Gradient Descent:

Random Forest:

K-Nearest Neighbors:

## Constraints / Limitiations

1. **Weak feature signal** - The ROC curve close to the diagnoal and modest AUC suggest that the features used contain limitied predictive information about the target. This is replicated across models
2. **High Class Overlap** - Threshold tuning yielded limited gains suggesting the positive and negative classes overlap heavily in feature space.
3. **Class Imbalance** - Model collapsed to predicting majority class if weighting was not used suggesting that there is a large class imbalance.
4. **Noisy Categorical Variables** - High cardinality and self reported categorical feautres introduced considerable noise.
5. **Cross-secitonal data** - the dataset does not support causal inference.
6. **Evaluation Scope** - The problem was not focused around a specific business objective. The ROC and AUC measures used did not have a cost-senstive threshold selection and utility-based evaluation was not possible.

## Conclusion

This project demonstrates a leakage-free end-to-end machine learning workflow applied to a low-signal, imbalanced classification problem. It highlights achievable performance gains within the structural limits imposed by the dataset used.

### Future Work

In general I consider the following avenues when coming back to this project that could refine it or expand its scope.

1. Incorporating the free-text attributes using natural language processing techniques.
2. Refining the research workflow into a more compact and easily read scikit-learn pipeline.

