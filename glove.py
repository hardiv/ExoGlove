# Setup RPi: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software

from adafruit_motorkit import MotorKit
import time


class Glove:
    def __init__(self):
        self.kit = MotorKit()
        # MotorKit: motor1, motor2, motor3, motor4
        self.top_fingers = self.kit.motor1
        self.top_thumb = self.kit.motor2
        self.bottom_fingers = self.kit.motor3
        self.bottom_thumb = self.kit.motor4
        self.tighten = True
        self.loosen = False
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
        multiplier = 1 if tighten is True else multiplier = -1
        self.top_fingers.throttle = multiplier*0.5

    def _move_bottom_fingers(self, tighten=True):
        multiplier = 1 if tighten is True else multiplier = -1
        self.top_fingers.throttle = multiplier*0.5

    def _move_top_thumb(self, tighten=True):
        multiplier = 1 if tighten is True else multiplier = -1
        self.top_fingers.throttle = multiplier*0.5

    def _move_bottom_thumb(self, tighten=True):
        multiplier = 1 if tighten is True else multiplier = -1
        self.top_fingers.throttle = multiplier*0.5

    def _haltAfter(self, num_secs):
        time.sleep(num_secs)
        self.top_fingers.throttle = 0
