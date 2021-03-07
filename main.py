import glove
import camera
import time
import classifier

g = glove.Glove()
grabbable_objects = ['handle', 'bottle', 'cup']


def isGripNeeded():
    photo = camera.take_photo()
    photo_class = classifier.classify(photo)  # svm by own dataset
    return photo_class in grababble_objects


while True:
    if isGripNeeded():
        g.gripObject(2)
        g.relax()
