# import glove
from classify import classifier
import camera
from datetime import datetime

# g = glove.Glove()
grabbable_objects = ['Cup', 'Handle', 'Bottle']
# grabbable_objects = ['Red', 'Green', 'Yellow', 'Not a']


def isGripNeeded():
    photo_file_path = camera.take_photo()
    photo_class, confidence = classifier.classify(photo_file_path)  # svm by own dataset
    print(photo_class)
    if photo_class in grabbable_objects:
        with open("tracking/activity.txt", "a") as activity_file:
            activity_file.write("\nPicked up a " + photo_class + " at " + str(datetime.now()) + ".") # format the date time
        return True


'''
while True:
    if isGripNeeded():
        g.gripObject(2)
        g.relax()
'''

print(isGripNeeded())
