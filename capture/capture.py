import camera
import RPi.GPIO as GPIO

pushbutton = 11
supply = 7


def buttonPressed(pin_number):
    return GPIO.input(pin_number) == GPIO.HIGH


def switchOn(pin_number):
    GPIO.output(pin_number, GPIO.HIGH)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(pushbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled
GPIO.setup(supply, GPIO.OUT)
# low (off)

switchOn(input)
count = 0  # Test
while True:  # Run forever
    if buttonPressed(pushbutton):  # Test 2
        print(f'Taking photo: {count}')
        print(f'Photo saved in location {camera.take_photo(0.05)}')
        count += 1
