import os
from classifier import *

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

image_to_classify = str(parent_dir) + '/assets/testing/' + input("Image name to classify: ") + '.jpg'
label, confidence = classify(image_to_classify)
print(f"The photo is a {label} with {confidence*100}% confidence")
