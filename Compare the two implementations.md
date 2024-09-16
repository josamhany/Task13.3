## Comparison Between Scratch, PyTorch, and TensorFlow Implementations

### 1. Ease of Use:
- **From Scratch**: Implementing everything from scratch gave me a deep understanding of how neural networks function internally, but it required significant effort and debugging.
- **PyTorch**: PyTorch provided a balance between control and convenience. I had to write the training loop explicitly, but its object-oriented nature made it easier to debug and experiment with.
- **TensorFlow (Keras)**: The Keras API was the simplest to use, requiring just a few lines of code to build, train, and evaluate the model. This is ideal for quick development.

### 2. Performance:
- **Scratch Implementation**: Without any optimizations, training the network took longer compared to the deep learning libraries.
- **PyTorch and TensorFlow**: Both frameworks performed similarly in terms of training speed and accuracy. TensorFlow had a slight edge in training speed, possibly due to its optimizations.

### 3. Flexibility:
- **PyTorch**: Offers great flexibility for custom architectures, dynamic changes, and low-level control over the training process.
- **TensorFlow (Keras)**: While easier to use, TensorFlow is less flexible for experimenting with novel architectures due to its high-level abstractions.

In summary, PyTorch is better suited for experimentation and research, whereas TensorFlow is ideal for fast development and deployment at scale.
