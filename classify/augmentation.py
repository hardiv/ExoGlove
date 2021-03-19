import matplotlib.pyplot as plt #for plotting a graph
import numpy as np #library for mathematical calculations in the form of arrays
import tensorflow as tf #library for numerical coding - supports nn
import tensorflow_datasets as tfds #importing the datasets - for ready to use datasets

from tensorflow.keras import layers #hidden layer in a nn
from tensorflow.keras.datasets import mnist #used for training models to recognise handwritten numbers,used for training images.
(train_ds, val_ds, test_ds), metadata = tfds.load(
    'beans',
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True,
) #3 types of results training validating(checking with different datasets) testing. metadata - data about data - features,labels
num_classes = metadata.features['label'].num_classes #gets the features and labels
print(num_classes)
get_label_name = metadata.features['label'].int2str

image, label = next(iter(train_ds))
_ = plt.imshow(image)
_ = plt.title(get_label_name(label))
IMG_SIZE = 180

resize_and_rescale = tf.keras.Sequential([
  layers.experimental.preprocessing.Resizing(IMG_SIZE, IMG_SIZE),
  layers.experimental.preprocessing.Rescaling(1./255)
]) #resizes and rescales all images
result = resize_and_rescale(image)
_ = plt.imshow(result)
print("Min and max pixel values:", result.numpy().min(), result.numpy().max())
data_augmentation = tf.keras.Sequential([
  layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
  layers.experimental.preprocessing.RandomRotation(0.2),=
])
# Add the image to a batch
image = tf.expand_dims(image, 0)
plt.figure(figsize=(10, 10))
for i in range(9):
  augmented_image = data_augmentation(image)
  ax = plt.subplot(3, 3, i + 1)
  plt.imshow(augmented_image[0])
  plt.axis("off")
