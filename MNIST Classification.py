## 2-MNIST Classification:
import numpy as np
import mnist

train_images = mnist.train_images() 
train_labels = mnist.train_labels()  
test_images = mnist.test_images()    
test_labels = mnist.test_labels()   

train_images = train_images.reshape(-1, 784) / 255.0
test_images = test_images.reshape(-1, 784) / 255.0

def one_hot_encode(labels, num_classes=10):
    one_hot_labels = np.zeros((len(labels), num_classes))
    for i, label in enumerate(labels):
        one_hot_labels[i, label] = 1
    return one_hot_labels

train_labels_one_hot = one_hot_encode(train_labels)
test_labels_one_hot = one_hot_encode(test_labels)
training_data = [(x.reshape(784, 1), y.reshape(10, 1)) for x, y in zip(train_images, train_labels_one_hot)]
test_data = [(x.reshape(784, 1), y) for x, y in zip(test_images, test_labels)]

network = NeuralNetwork([784, 30, 10])  # Example 

network.train(training_data, epochs=30, mini_batch_size=10, eta=3.0, test_data=test_data)