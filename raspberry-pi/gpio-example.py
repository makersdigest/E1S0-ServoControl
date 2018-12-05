##
 # Maker's Digest
 # GPIO Python Servo Example
 # 
 # Dont forget to install scipy! See README.md for details
## 
import RPi.GPIO as GPIO     # Import GPIO Module
from time import sleep      # Import Sleep module from time library
from scipy.interpolate import interp1d  # Import interpolation from scipy

pin = 18                    # Set GPIO pin 18 on raspberry pi
dly = .5                    # Set delay to 500ms (half second (.5))

GPIO.setmode(GPIO.BCM)      # Set mode of GPIO
GPIO.setup(pin, GPIO.OUT)   # Set pin to Output

# Servo expects a pulse every 20ms, thats 50 pulses per second
# 1000ms / 20 = 50 (50 Hertz)
servo = GPIO.PWM(pin, 50)     # Set GPIO pin 18 to 50hz PWM.
servo.start(2.5)              # PWM start. Duty cycle 2.5ms.

# Setup interpolation. To determine the dc_range, follow the instructions in 
# the README.md. dc_range is the Duty Cycle Range, and deg_range is the range
# of your servo. Leave at 180 if your servo is 180. 
dc_range = [2, 13]
deg_range = [0, 180]
interp_degrees = interp1d(deg_range, dc_range)

# This method takes input of degrees, converts it to duty cycle, sets the
# GPIO output to true, changes the dutycycle of the servo, waits for a period
# so that the servo has time to move, then sets GPIO output to False, and 
# sets the duty cycle to 0 so that the servo does not jitter.
def setAngle(angle):
    duty = interp_degrees(angle)
    GPIO.output(pin, True)      # Set output to True
    servo.ChangeDutyCycle(duty)   # Set the duty cycle from argument
    sleep(dly)                  # Sleep so the servo has time to move
    GPIO.output(pin, False)     # Set output to false
    servo.ChangeDutyCycle(0)      # Set duty cycle to 0

# The example
def main(args=None):
    try:
        while True:
            setAngle(0)
            setAngle(90)
            setAngle(180)
            setAngle(90)
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
        
if __name__ == "__main__":
    main()


