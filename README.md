# Task13.3
# Neural Network from Scratch

## Overview

This project implements a basic feedforward neural network from scratch, based on Chapter 1 of Michael Nielsen's book, *Neural Networks and Deep Learning*. The network is trained using mini-batch stochastic gradient descent and backpropagation without any deep learning libraries.

### Key Concepts

- **Neural Network Structure**:
  - The network consists of layers of neurons, each connected to the neurons in the next layer via weights. Each neuron has a bias that influences the output.
  
- **Activation Function**:
  - The network uses the sigmoid activation function to map weighted sums of neuron inputs to a non-linear output.
  - Formula: 
    \[
    \sigma(z) = \frac{1}{1 + e^{-z}}
    \]
  
- **Cost Function**:
  - The quadratic cost function is used to measure the difference between predicted and actual output:
    \[
    C = \frac{1}{2n} \sum_{x} || y(x) - a ||^2
    \]
  
- **Backpropagation**:
  - Backpropagation is used to compute the gradients of the cost function with respect to weights and biases.
  - The error is propagated backwards through the network to update the parameters.
  
- **Stochastic Gradient Descent**:
  - The network is trained using mini-batch stochastic gradient descent (SGD), which divides the training data into small batches to efficiently update weights and biases.

### Implementation Details

- **Classes**:
  - `NeuralNetwork`: The main class that implements the feedforward, backpropagation, and training methods.
  
- **Training**:
  - The network is trained over multiple epochs using mini-batches.
  - Weights and biases are updated using the computed gradients from backpropagation.

### Future Work

- Implement regularization techniques such as L2 or dropout to improve generalization.
- Explore different activation functions like ReLU.
- Investigate advanced optimization techniques like Adam.

### Reference

- *Neural Networks and Deep Learning* by Michael Nielsen
- *Cahtgpt*
