# Predicting Medical Proffessionals From OkCupid Profile Data

## Problem Statement
Presented with a dataset of self reported of users self-reported characteristics taken from a dating platform, can we build a binary classifier model that will predict whether a user works in the medical profession?

## Data
The dataset used is the OkCupid Dataset available [here](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles).

The dataset consists of self-reported demographic and behavioural attributes taken from an online dating platform.

Size of the dataset is 31 attributes with 59,946 entries.

2 attributes are numerical, 10 are free-text attributes, 1 is date-time, 1 is geospatial, 17 are categorical or ordinal.

It is important to note that this dataset does not include any identifying characteristics.

It should also be noted that the target variable exhibits significant class imbalance, with medical professionals representing a minority of observations.

## Methodology

### Performance Measure
As the problem is a classification problem, the performance measures chosen are:
1. Confusion Matrix
2. Reciver Operating Characteristic (ROC) Curve - Area under the curve (AUC)

Due to the class imbalance accuracy will not be used as a metric as it would overstate performance by favoring the majority class.

### Assumptions
1. The train/test split method is representative and will produces two subsets drawn from the underlying distribution.
2. Observations are independent and each row represents an independent individual.
3. The labels in the dataset are reliable.
4. The preprocessing correctly encodes and preserves the feature semantics of the original variables.

### Leakage Control
A fixed train/test split was created prior to preprocessing to prevent data leakage.

### Reproducibility

Random seeds are fixed where applicable.  
To reproduce results:
1. Download the dataset from Kaggle.
2. Place profiles.csv in the data/ directory.
3. Install requirements.txt.
4. Run notebooks/analysis.ipynb.

## Results

All models demonstrated comparable performance after hyperparamter optimization using GridSearchCV.

Final AUC's on the Test Set:
Stochastic Graident Descent: 0.669
Random Forest Classifier: 0.684
K-Nearest Neighbor: 0.650

## Constraints / Limitiations

1. **Weak feature signal** - The ROC curves and modest AUC values suggest that the features used contain limitied predictive information about the target. This is replicated across models
2. **High Class Overlap** - Threshold tuning yielded limited gains suggesting the positive and negative classes overlap heavily in feature space.
3. **Class Imbalance** - Models collapsed to predicting majority class if balanced weighting was not used.
4. **Noisy Categorical Variables** - High cardinality and self reported categorical feautres introduced considerable noise.
5. **Cross-secitonal data** - The dataset does not support causal inference.
6. **Evaluation Scope** - The problem was not focused around a specific business objective. The ROC and AUC measures used did not have a cost-senstive threshold selection and utility-based evaluation was not possible.

## Conclusion

This project demonstrates a leakage-free end-to-end machine learning workflow applied to a low-signal, imbalanced classification problem. It highlights achievable performance gains within the structural limits imposed by the dataset used.

### Future Work

The following are avenues of future refinement or expansion in scope.

1. Incorporating the free-text attributes using natural language processing techniques.
2. Refining the research workflow into a more compact and easily read scikit-learn pipeline.
3. Expanding the classification problem into multi-class classification.