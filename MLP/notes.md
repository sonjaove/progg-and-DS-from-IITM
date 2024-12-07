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
    ```python
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