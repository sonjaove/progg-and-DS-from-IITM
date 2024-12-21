## generic points.
- make a baseline model, which can be made via ```sklearn.dummy``` 
```py 
from sklearn.dummy import DummyRegressor

dummy_regr = DummyRegressor(strategy="mean")
dummy_regr.fit(X_train, y_train)
dummy_regr.predict(X_test)
dummy_regr.score(X_test, y_test)
'''
It makes a prediction as specified by the strategy.
Strategy is based on some statistical property of the
training set or user specified value.
'''
```
- for normal eq, use,
```py
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
```
- for iterative optimization, use,
```py
from sklearn.linear_model import SGDRegressor
linear_regressor = SGDRegressor()
```
- Works for both single and multi-output regression.
- make a habit of referring the docs.
---
## SGDRegressor Estimator
- impliments stocastic gradient descent algo, better suited for datasets with large number of samples(>10k samples)
- Provides greater control on optimization process through provision for hyperparameter settings.   
- [THE HYPERPARAMETERS!!](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)
- It's a good idea to use a random seed of your choice while instantiating SGDRegressor object. It helps us get reproducible results, always set the random seed in the constructor.
- you can shuffle traning data after every epoch using the *shuffle* parameter.
- SDG is highly sensitive to scale, so make sure to scale your features to a common scale before fitting the model.
- ***Feature scaling is not needed for word frequencies and indicator features as they have intrinsic scale.***
- Features extracted using PCA should be scaled by some constant such that the average L2 norm of the training data equals one. 
- the default setting is 
learning_rate = 'invscaling', eta0 = 1e-2, power_t = 0.25, which means 
    - Learning rate reduces after every iteration:
        **eta = eta0 / pow(t, power_t)**
- for adaptive leraning:
```py 
from sklearn.linear_model import SGDRegressor
linear_regressor = SGDRegressor(learning_rate='adaptive',eta0=1e-2)
'''
The learning rate is kept to initial value as long as the training loss
decreases.

When the stopping criterion is reached, the learning rate is divided
by 5, and the training loop continues.

The algorithm stops when the learning rate goes below 10^-6 .
'''
```
- SGD converges after observing approximately 10^6 training samples. Thus, a reasonable first guess for the number of iterations for sampled training set is ***max_iter = np.ceil(10^6/n)***
- Averaged SGD updates the weight vector to average of weights from previous updates, works best with a larger number of features and a higher eta0
- monitering loss:
    - use for loop.
    ```py
    sgd_reg = SGDRegressor(max_iter=1, tol=-np.infty, warm_start=True,
    penalty=None, learning_rate="constant", eta0=0.0005)
    for epoch in range(1000):
    sgd_reg.fit(X_train, y_train) # continues where it left off
    y_val_predict = sgd_reg.predict(X_val)
    val_error = mean_squared_error(y_val, y_val_predict)
    # at this stage after the loop you can plot a loss curve as well.
    ```
