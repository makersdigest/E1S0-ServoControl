##
 # Maker's Digest
 # Servo Control
##
from time import sleep
import wiringpi
from scipy.interpolate import interp1d

pin = 18

pw_range = [50, 260]
deg_range = [0, 180]
interp_degrees = interp1d(deg_range, pw_range)

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

def setServoDegrees(deg):
    wiringpi.pwmWrite(pin, int(interp_degrees(deg)))
    sleep(0.5)
    wiringpi.pwmWrite(pin, 0)
    
try:
    while True:
        setServoDegrees(0)
        setServoDegrees(90)
        setServoDegrees(180)
        setServoDegrees(90)
except KeyboardInterrupt:
    quit()

