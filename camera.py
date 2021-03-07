from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0
camera.resolution = (2592, 1944)  # max
camera.resolution = (64, 64)  # min
camera.framerate = 15
camera.image_effect = 'film'  # grayscale

# Set transparency
camera.start_preview(alpha=0)
sleep(5)
camera.stop_preview()

# Take 5 pictures
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('image%s.jpg' % i)
camera.stop_preview()

# record video
camera.start_preview()
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
