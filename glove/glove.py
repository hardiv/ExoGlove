# Setup RPi: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software

import time
import board
from adafruit_motorkit import MotorKit
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 27
GPIO_ECHO = 22
GPIO.setup(GPIO_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled
GPIO.setup(18, GPIO.OUT)


class Glove:
    def __init__(self):
        self.kit = MotorKit(i2c=board.I2C())
        # MotorKit: motor1, motor2, motor3, motor4
        self.top_fingers = self.kit.motor1
        self.top_thumb = self.kit.motor2
        self.bottom_fingers = self.kit.motor3
        self.bottom_thumb = self.kit.motor4
        self.tighten = True
        self.loosen = False
        self.ultrasonic = 0  # For Ultrasonic sensor
        # Driving any motors +ve will tighten the string they are attached to and vice versa

    def gripObject(self, time_to_grip=1):
        self._move_top_fingers(self.loosen)
        self._move_bottom_fingers(self.tighten)
        time.sleep(1)
        self._move_top_thumb(self.loosen)
        self._move_bottom_thumb(self.tighten)
        self._haltAfter(time_to_grip)

    def relax(self, time_to_grip=1):
        self._move_top_thumb(self.tighten)
        self._move_bottom_thumb(self.loosen)
        time.sleep(1)
        self._move_top_fingers(self.tighten)
        self._move_bottom_fingers(self.loosen)
        self._haltAfter(time_to_grip)

    def _move_top_fingers(self, tighten=True):
        if tighten is True:
            multiplier = 1
        else:
            multiplier = -1
        self.top_fingers.throttle = multiplier*0.5

    def _move_bottom_fingers(self, tighten=True):
        if tighten is True:
            multiplier = 1
        else:
            multiplier = -1
        self.bottom_fingers.throttle = multiplier*0.5

    def _move_top_thumb(self, tighten=True):
        if tighten is True:
            multiplier = 1
        else:
            multiplier = -1
        self.top_thumb.throttle = multiplier*0.5

    def _move_bottom_thumb(self, tighten=True):
        if tighten is True:
            multiplier = 1
        else:
            multiplier = -1
        self.bottom_thumb.throttle = multiplier*0.5

    def getDist(self):
        print("Getting Distance...")
        return 3
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
            print(GPIO.input(GPIO_ECHO))
        # save time of arrival
        print("Exited loop 1")
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
            print(GPIO.input(GPIO_ECHO))
        print("Exited loop 2")
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        return distance

    def _haltAfter(self, num_secs):
        time.sleep(num_secs)
        self.top_fingers.throttle = 0
        self.bottom_fingers.throttle = 0
        self.top_thumb.throttle = 0
        self.bottom_thumb.throttle = 0


# Unit testing for hardware
if __name__ == "__main__":
    glove = Glove()
    print("Tightening")
    glove.gripObject()
    print("Loosening")
    glove.relax()
    # sensor
    dist = glove.getDist()
    print("Measured Distance = %.1f cm" % dist)
    time.sleep(1)
