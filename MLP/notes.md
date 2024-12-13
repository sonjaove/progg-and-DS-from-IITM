## Generic points:

1. stratified sampling vs random smapling 
2. EDA can be performed after splitting as well simply on the train set.
3. Exploration is an iterative process: Once we build model and obtain more insights,

we can come back to this step.

4. min-max scalling(bounds the values between 0 and 1, while variance is <1 ) is different from standard scalling(does not bound the values between 0 and 1, varience = 1).
5. ***Never learn these transformers on the full dataset.***

## Pipeline 

1. Pipeline has a sequence of transformations - missing value imputation followed by

standardization.

2. Each step in the sequence is defined by name, estimator pair.
3. Each name should be unique and should not contain __ (double underscore).

```python
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    transform_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
    ('std_scaler', StandardScaler()),])
    wine_features_tr = transform_pipeline.fit_transform(wine_features)
```

4. The output of one step is passed on the next one in sequence until it reaches the last

step.

5. The pipeline exposes the same method as the final estimator.

   - Here StandardScalar is the last estimator and since it is a transformer, we call

       fit_transform() method on the Pipeline object.
6. for mixed columns:
    1. use ColumnTransform:

```py
from sklearn.compose import ColumnTransformer
```

- We can use cross-validation (CV) for robust evaluation of model performance.
- Cross validation provides a separate MSE for each validation set, which we can

use to get a mean estimation of MSE as well as the standard deviation, which

helps us to determine how precise is the estimate.

- select and trian your model first, analyze the validation scores and then for hyperparameter tunning use GridSearchCV.
- It's a good idea to get 95% confidence interval of the evaluation metric. It can be

obtained by the following code:

```python
    from scipy import stats
    confidence = 0.95
    squared_errors = (quality_test_predictions - wine_labels_test) ** 2
    stats.t.interval(confidence, len(squared_errors) - 1,
    loc=squared_errors.mean(),
    scale=stats.sem(squared_errors))
```

# Preferred preprocessing steps:

## 1. Data cleaning - standardization, missing value imputation.
- refre from the slides itself (week 3.), ***knn-imputer***

## 2. feature extraction - bascially an umbrella term for feature reduction and expansion.
1. DictVectorizer:
    - Converts lists of mappings of feature name and feature
    value, into a matrix.
    ```python
    from sklearn.feature_extraction import DictVectorizer
    dv = DictVectorizer(sparse=False) # if sparese=True, then it'll return a sparse matrix in a format like CSR (Compressed Sparse Row) to save memory, so it'll be returned as an object.
    dv.fit_transform(data)
    ```
2. FeatureHasher:
    - High-speed, low-memory vectorizer that uses feature
    hashing technique. 
    - hashtable=dict/json.
    - it applies a hash function to the features
    to determine their column index in sample matrices
    directly.(dunno how thats more efficient.)This results in increased speed and reduced memory
    usage, at the expense of inspectability; the hasher does
    not remember what the input features looked like and
    has no inverse_transform method.
    - Output of this transformer is scipy.sparse matrix.

3. Feature reduction - essentially means reducing data to a lower dimenssion feature space.

4. Feature expansion - essentially means moving data to a higher dimenssion feature space.

## 3. Feature selection:
- The features that do not contribute significantly, can be
removed. It leads to decrease in size of the dataset and
hence, the computation cost of fitting a model.
- there are 2 categories, namely:
1. wrapper based:
    - wrapper based methods use estimator class rather than a scoring function.
    1. RFE (Recursive Feature Elimination):
    - first fits an estimator on the data then decides on the importance of each feature, removes the least important feature, repeasts this recursively untll desired number of features are obtained.

    - Use RFECV if we do not want to specify the desired number of features in RFE eg. 
    ```py
    from sklearn.svm import LinearSVC
    from sklearn.feature_selection import RFE

    # Initialize the model
    clf = LinearSVC(C=0.01, penalty="l1", dual=False)

    # Use RFE for recursive feature elimination
    rfe = RFE(estimator=clf, n_features_to_select=5)  # Adjust the number of features to select

    # Fit RFE on the data
    rfe = rfe.fit(X, y)

    # Transform the dataset to select only the important features
    X_new = rfe.transform(X)

    # Check selected features
    print(rfe.support_)  # Boolean mask of selected features
    print(rfe.ranking_)  # Feature ranking

    ```
    2. SelectFromModel:
    - Selects desired number of important features (as specified with max_features parameter) above certain threshold of feature importance as obtained from the trained estimator. The feature importance is obtained via coef_,              feature_importances_ or an importance_getter callable from the trained estimator.

    - The feature importance threshold can be specified either numerically or through string argument based on built-in heuristics such as 'mean', 'median' and float multiples of these like '0.1*mean' eg.
    ```py
    from sklearn.svm import LinearSVC
    from sklearn.feature_selection import SelectFromModel

    # Train a LinearSVC model with L1 regularization for feature selection
    clf = LinearSVC(C=0.01, penalty="l1", dual=False, max_iter=5000)
    clf.fit(X, y)

    # Use SelectFromModel to select important features
    model = SelectFromModel(clf, prefit=True)
    X_new = model.transform(X)

    print(X_new.shape)  # Check the shape after feature selection
    ```
    3. Sequential feature selection:
    

2. filter based:
    1. Removing features with low variance:
        - this includes ***VarinceThreshold***, which removes all features with variance below a certain threshold, as specified by the user, from input feature matrix.

        - By default removes a feature which has same value, i.e. zero variance.

    2. Univariate feature selection:
        - selects features based on univariate statistical tests(need examples)
        - [APIs for UFS: SelectKBest, SelectPercentile, GenericUnivariateSelect.](https://scikit-learn.org/stable/api/sklearn.feature_selection.html)
        - ### Univariate scoring function:
            - there are three main classes of scoring functions namely:
                1. Mutual Information - Measures dependency between two variables. It returns a non-negative value.
                    - MI = 0 for independent variables.
                    - Higher MI indicates
                    higher dependency.
                2. chi-sq - used only in classification tasks, and is used to measure dependence b/w 2 non-negative
                feature (boolean or frequencies) and class label. Higher chi-square values indicates that the features and labels are likely to be correlated.
                3. F-statistic
            - a and c can be used in both classification and regression task.
            - MI and chi-squared feature selection is recommended for sparse data.
            - ***Do not use regression feature scoring function with a classification problem. It will lead to useless results.***