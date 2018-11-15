import RPi.GPIO as GPIO
from time import sleep

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 50)     # Set GPIO pin 18 to 50hz PWM.
pwm.start(2.5)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        setAngle(0)
        sleep(1)
        setAngle(180)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()


