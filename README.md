# Tensorflow on MNIST Data

## Background
The objective of this project is to learn the fundamental mechanisms of a machine learning application through a simple use-case of classifying handwritten numbers.

Several techniques of Machine Learning will be attempted on the dataset. This repo tests the **[Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)** method, a Supervised Learning technique trained by the random incremental gradient descent algorithm. This is an iterative and coarse approach to locating the global maximum/minimum.

## Model Results
See **[Stochastic Gradient Descent](Evaluations.md)**

## Get Started
```
python app.py
```

## Steps
- Download and prime the input training data set of 60,000 images and 10,000 labels.
- Initiate a Tensorflow (TF) session with basic configuations (e.g. image size, learning rate, number of steps).
- "Train" the TF model with the input data.
  - The model will kick off computations with 1.0 as the initial for the biases, and a normal distribution of values for the initial weights.
  - TF will evaluate the error rate of the computed values from expected values (from the label training data).
  - TF will run several "generations" of computations with calibrated weights and biases to minimize the error rate, yielding the best fit linear model.
- Experiment with calibrations in configurations like learning rate, step numbers, etc. to reduce error even further.
- Once a model under a satisfactory threshold of error is created, apply it to the test data set.

## Technologies
- [Tensorflow](https://www.tensorflow.org/)
- [MNIST](http://yann.lecun.com/exdb/mnist/) Handwritten Numbers Data

