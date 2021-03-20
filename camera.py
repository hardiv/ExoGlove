from picamera import PiCamera
from time import sleep

camera = PiCamera()
image_count = 0
video_count = 0

# Setup
camera.rotation = 0
# camera.resolution = (2592, 1944) - maximum
# camera.resolution = (64, 64) - minimum
camera.resolution = (64, 64)
camera.framerate = 15
# camera.image_effect = 'film' - grayscale

# Set transparency
camera.start_preview(alpha=0)
sleep(5)
camera.stop_preview()


def reset():
    global image_count
    image_count = 0


def take_photo(time_delay=1):
    global image_count
    filename = '/home/pi/_code/Python/ExoGlove/assets/testing/Simage%s.jpg' % image_count
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
