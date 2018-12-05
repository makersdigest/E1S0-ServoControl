##
 # Maker's Digest
 # WiringPI Servo Example
 #
 # Dont forget to install wiringpi and scipy! See README.md for details
##
import wiringpi         # Import Wiringpi module
from time import sleep  # Import sleep from time module
from scipy.interpolate import interp1d  # scipy for interpolation

pin = 18                # Using pin 18 on Raspberry Pi
dly = .5                # 500ms Delay

# Here we are going to setup our interpolation ranges.
# To determine the pw_range, follow the directions in the README.md
# deg_range, is the range of your servo. Leave as is if it is a 180 degree servo
pw_range = [50, 260] 
deg_range = [0, 180]
interp_degrees = interp1d(deg_range, pw_range)

# Setting up wiringpi. We are setting the pinmode to PWM Output, 
# PWM Mode to MS (milliseconds), Clock and range set as they are 
# tell wiringpi to run at 50hz. 
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

# This method takes input of degrees, converts it to pulse width,
# waits half a second, then sets the pulse width to 0. In wiringpi
# setting the pulsewidth to zero essentially turns off the servo. 
# otherwise it will be jittery. 
def setAngle(deg):
    wiringpi.pwmWrite(pin, int(interp_degrees(deg)))
    sleep(dly)
    wiringpi.pwmWrite(pin, 0)
    
# run the example. 0 -> 90 -> 180 -> 90 -> 0 ...
def main(args=None):
    try:
        while True:
            setAngle(0)
            setAngle(90)
            setAngle(180)
            setAngle(90)
    except KeyboardInterrupt:
        wiringpi.pwmWrite(pin,0)

if __name__ == "__main__":
    main()
