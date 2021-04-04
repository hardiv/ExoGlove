import os
import sys
from time import sleep
from picamera import PiCamera

# File path Setup
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)  # going to the parent directory
print("Went to parent directory", parentdir)


# Camera Setup
camera = PiCamera()
image_count = 0
video_count = 0
camera.rotation = 0
# camera.resolution = (2592, 1944) - maximum
# camera.resolution = (64, 64) - minimum
camera.resolution = (256, 256)
camera.framerate = 15
# camera.image_effect = 'film' - grayscale


def reset():
    global image_count
    image_count = 0


def take_photo(time_delay=1):
    global image_count
    filename = str(parentdir) + 'assets/testing/image%s.jpg' % image_count
    # filename = '/home/pi/Pictures/image%s.jpg' % image_count
    camera.capture(filename)
    sleep(time_delay)
    image_count += 1
    return filename


def record_video(time_delay):
    camera.start_preview()
    camera.start_recording('video%s.h264' % video_count)
    sleep(time_delay)
    camera.stop_recording()
    camera.stop_preview()


if __name__ == '__main__':
    camera.start_preview(alpha=0)  # alpha sets transparency
    sleep(5)
    camera.stop_preview()
