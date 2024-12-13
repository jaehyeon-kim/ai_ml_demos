## 02 Launching into Machine Learning

```
Accuracy = (TP + TN) / (TP + FP + FN + TN)

What proportion of positive identifications was actually correct?
Precision = TP / (TP + FP)

What proportion of actual positive was identified correctly?
Recall = TP / (TP + FN)
                          Actual
                   Positive | Negative
          Positive    TP        FP
Predicted
          Negative    FN    |   TN


                         Prediction
                   Positive | Negative
          Positive    TP        FN
Actual
          Negative    FP    |   TN


FN --> Type II error
FP --> Type I error
```

### Module 5: Optimization

**Gradient Descent Algorithms**

- `Stochastic Gradient descent` is a variation of the gradient descent algorithm that calculates the error and updates the model for each example in the training dataset.
- `Batch gradient descent` is a variation of the gradient descent algorithm that calculates the error for each example in the training dataset, but only updates the model after all training examples have been evaluated.
- `Mini-batch gradient descent` is a variation of the gradient descent algorithm that splits the training dataset into small batches that are used to calculate model error and update model coefficients.

**Tensorflow Playground**

- [Example 1](https://goo.gl/EEuEGp)
- [Example 2](https://goo.gl/ou9iMB)
- [Example 3](https://goo.gl/1v28Pd)
- [Example 4](https://goo.gl/VyoRWX)
- [Example 5](https://goo.gl/hrXd9T)
- [Example 6](https://goo.gl/iSY7rB)

**Model Validation**

- If you have lots of data, use a held-out test dataset.
- If you have little data, use cross-validation.

## General

- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
