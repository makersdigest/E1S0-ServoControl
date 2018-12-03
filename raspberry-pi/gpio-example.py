##
 # Maker's Digest
 # Python Servo Example
## 
import RPi.GPIO as GPIO     # Import GPIO Module
from time import sleep      # Import Sleep module from time library

pin = 18                    # Set GPIO pin 18 on raspberry pi
dly = .5                    # Set delay to 500ms (half second (.5))

GPIO.setmode(GPIO.BCM)      # Set mode of GPIO
GPIO.setup(pin, GPIO.OUT)   # Set pin to Output

# Servo expects a pulse every 20ms, thats 50 pulses per second
# (50 Hertz)
pwm = GPIO.PWM(pin, 50)     # Set GPIO pin 18 to 50hz PWM.
pwm.start(2.5)              # PWM start. Duty cycle 2.5ms.

# To change the angle of the servo we need to change the duty cycle
# we are sending to the servo. The duty cycle describes the porportion
# of ON time to the regular interval of time. 

# We can caluclate this with the following:
# duty_cycle = (length / period)
# Lenth is length of time the pulse is on, period is 20ms per cycle.
# duty_cycle = (2.5 / 20);

# Since there is a little math that needs to be done
# each time we set an angle on the servo in python
# it makes sense to create a method that handles
# the math, turns the pin on and off, sets the duty cycle
# and cleans up.
def setAngle(angle):
    duty = angle / 18 + 2       # Da Math
    GPIO.output(pin, True)      # Set output to True
    pwm.ChangeDutyCycle(duty)   # Set the duty cycle from argument
    sleep(1)                    # Sleep for one second so the servo can move
    GPIO.output(pin, False)     # Set output to false
    pwm.ChangeDutyCycle(0)      # Set duty cycle to 0

try:
    while True:
        setAngle(0)
        sleep(dly)
        setAngle(90)
        sleep(dly)
        setAngle(180)
        sleep(dly)
        setAngle(90)
        sleep(dly)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()


