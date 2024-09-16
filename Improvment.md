## Neural Network Improvements

### 1. Optimizer: Adam vs. SGD
- Replaced stochastic gradient descent (SGD) with the Adam optimizer.
- **Results**: Adam achieved faster convergence and better stability, particularly with larger learning rates.

### 2. Weight Initialization: He Initialization
- Changed the weight initialization method to He initialization, designed for ReLU activation.
- **Results**: Faster convergence and more stable learning.

### 3. Regularization: L2 Regularization and Dropout
- Added L2 regularization (weight decay) to penalize large weights.
- Implemented Dropout (50%) to reduce overfitting.
- **Results**: Improved test accuracy and reduced overfitting, especially when the model was prone to overfitting with a small dataset.
