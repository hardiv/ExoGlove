import camera
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled
# low (off)

count = 0  # Test
while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:  # Test 2
        print(f'Taking photo: {count}')
        print(f'Photo saved in location {camera.take_photo(0.1)}')
        count += 1
