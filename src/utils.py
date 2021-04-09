from classify import classifier
from capture import camera
from datetime import datetime

grabbable_objects = ['Cup', 'Handle', 'Bottle']


def format_date(date):
    time = date[0]
    date = date[1]
    return str(time) + " " + str(date)


def isGripNeeded():
    photo_file_path = camera.take_photo()
    photo_class, confidence = classifier.classify(photo_file_path)  # svm by own dataset
    print(photo_class)
    if photo_class in grabbable_objects:
        with open("tracking/activity.txt", "a") as activity_file:
            activity_file.write("\nPicked up a " + photo_class + " at " + format_date(str(datetime.now())) + ".")
        return True
