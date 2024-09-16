import tensorflow as tf
from tensorflow.keras import layers, models
import torch.nn.init as init

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch_size=64)

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu', kernel_initializer='he_uniform'),
    layers.Dense(64, activation='relu', kernel_initializer='he_uniform'),
    layers.Dense(10, activation='softmax')
])
from tensorflow.keras import regularizers

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu', kernel_initializer='he_uniform',
                 kernel_regularizer=regularizers.l2(1e-4)), 
    layers.Dense(64, activation='relu', kernel_initializer='he_uniform',
                 kernel_regularizer=regularizers.l2(1e-4)),
    layers.Dropout(0.5), 
    layers.Dense(10, activation='softmax')
])

