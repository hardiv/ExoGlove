import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


def get_most_probable_label(prediction):
	pass


def classify(image_to_test):
	# Disable scientific notation for clarity
	np.set_printoptions(suppress=True)

	# Load the model
	model = tensorflow.keras.models.load_model('classify/converted_keras/keras_model.h5')

	# Create the array of the right shape to feed into the keras model
	# The 'length' or number of images you can put into the array is
	# determined by the first position in the shape tuple, in this case 1.
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
	# Opens Specified Image
	image = Image.open(image_to_test)

	# resizing the image to be at least 224x224 and then cropping from the center
	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)

	# turn the image into a numpy array
	image_array = np.asarray(image)

	# display the resized image
	image.show()

	# Normalize the image (convert values to between 0 and 1)
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

	# Load the image into the array
	data[0] = normalized_image_array

	# run the inference
	prediction = model.predict(data)
	red_confidence = prediction[0][0]
	yellow_confidence = prediction[0][1]
	green_confidence = prediction[0][2]
	other_confidence = prediction[0][3]

	# print(red_confidence, yellow_confidence, green_confidence, other_confidence)

	highest_confidence = max(red_confidence, green_confidence, yellow_confidence, other_confidence)

	image_label = "Other"
	if highest_confidence == red_confidence:
		image_label = "Cup"
	elif highest_confidence == green_confidence:
		image_label = "Handle"
	elif highest_confidence == yellow_confidence:
		image_label = "Bottle"

	return image_label, highest_confidence
