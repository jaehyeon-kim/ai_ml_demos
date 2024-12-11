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

### Module 1: Get to Know Your Data: Improve Data through Exploratory Data Analysis

- [Guide to Data Quality Management](https://www.scnsoft.com/blog/guide-to-data-quality-management)
- [Exploratory Data Analysis With Python](https://www.youtube.com/watch?v=-o3AxdVcUtQ)
- [How to investigate a dataset with python?](https://towardsdatascience.com/hitchhikers-guide-to-exploratory-data-analysis-6e8d896d3f7e)

### Module 2: Machine Learning in Practice

- [Supervised and Unsupervised Machine Learning Algorithms ](https://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/)
- [Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning#:~:text=Supervised%20learning%20is%20the%20machine,a%20set%20of%20training%20examples.)
- [What the Hell is Perceptron?](https://towardsdatascience.com/what-the-hell-is-perceptron-626217814f53)
- [What is Perceptron: A Beginners Tutorial for Perceptron](https://www.simplilearn.com/what-is-perceptron-tutorial#:~:text=A%20perceptron%20is%20a%20neural,on%20the%20original%20MCP%20neuron.)
- [Perceptrons](https://deepai.org/machine-learning-glossary-and-terms/perceptron)
- [Understanding the perceptron neuron model](https://www.neuraldesigner.com/blog/perceptron-the-main-component-of-neural-networks)
- [Machine Learning for Beginners: An Introduction to Neural Networks ](https://towardsdatascience.com/machine-learning-for-beginners-an-introduction-to-neural-networks-d49f22d238f9)
- [What is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk)
- [Neural Networks and Deep Learning](https://pathmind.com/wiki/neural-network)
- [Decision Trees and Random Forests](https://towardsdatascience.com/decision-trees-and-random-forests-df0c3123f991)
- [Decision Tree vs. Random Forest – Which Algorithm Should You Use? ](https://www.analyticsvidhya.com/blog/2020/05/decision-tree-vs-random-forest-algorithm/)
- [Decision Tree and Random Forest](https://medium.com/datadriveninvestor/decision-tree-and-random-forest-e174686dd9eb)
- [Kernel Methods](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/kernel-method)
- [Kernel Methods](https://link.springer.com/chapter/10.1007/978-3-662-43505-2_32)
- [Modern Neural Networks Generalize on Small Data Sets](https://papers.nips.cc/paper/7620-modern-neural-networks-generalize-on-small-data-sets)
- [Neural Network Architectures for Machine Learning Researchers](https://medium.com/cracking-the-data-science-interview/a-gentle-introduction-to-neural-networks-for-machine-learning-d5f3f8987786)

### Module 3: Training AutoML Models Using Veex AI

- [Training AutoML Models](https://cloud.google.com/vertex-ai/docs/training/training)
- [Train an AutoML Model (Cloud Console)](https://cloud.google.com/vertex-ai/docs/training/automl-console)
- [Train an AutoML Model (API)](https://cloud.google.com/vertex-ai/docs/training/automl-api)
- [Optimization objectives for tabular AutoML models](https://cloud.google.com/vertex-ai/docs/training/tabular-opt-obj)
- [Train an AutoML Edge model using the Cloud Console](https://cloud.google.com/vertex-ai/docs/training/automl-edge-console)
- [Train an AutoML Edge model using the Vertex AI API](https://cloud.google.com/vertex-ai/docs/training/automl-edge-api)
- [Evaluate AutoML Models](https://cloud.google.com/vertex-ai/docs/training/evaluating-automl-models)

### Module 4: BigQuery Machine Learning: Develop ML Models Where Your Data Lives

- [BigQuery ML](https://cloud.google.com/bigquery-ml/docs)
- [Creating and Training Models](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create)
- [BigQuery ML Hyperparameter Tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview)
- [BigQuery ML Model Evaluation Overview](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-evaluate-overview)

### Module 5: Optimization

- [Introduction to Linear Models](https://genomicsclass.github.io/book/pages/intro_using_regression.html)
- [Linear Models](https://www.sciencedirect.com/topics/mathematics/linear-models)
- [How to Choose a Machine Learning Model – Some Guidelines](https://www.datasciencecentral.com/profiles/blogs/how-to-choose-a-machine-learning-model-some-guidelines)
- [How to Choose Loss Functions When Training Deep Learning Neural Networks](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/)
- [4 Common Pialls in Puing a Machine Learning Model in Production](https://www.topbots.com/pitfalls-in-putting-ml-model-in-production/)
- [Peormance Metric](https://www.sciencedirect.com/topics/computer-science/performance-metric)
- [Understanding Confusion Matrix](https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62)

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

### Module 6: Generalization and Sampling

- [When to stop Training your Neural Network?](https://medium.com/@pranoyradhakrishnan/when-to-stop-training-your-neural-network-174ff0a6dea5)
- [Generalization, Regularization, Oveiing, Bias and Variance in Machine Learning](https://towardsdatascience.com/generalization-regularization-overfitting-bias-and-variance-in-machine-learning-aa942886b870)

## General

- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
