# Maker's Digest
## Raspberry Pi Servo Control
We are going to look at two different methods of controlling servos. The first example `gpio-example.py` uses the standard RPi.GPIO library. I personally prefer wiringpi. The second example `wiringpi-example.py` shows how to utilize this library.

## Installation
These examples require software. Follow the instructions below to install the correct utilities and libraries.

`sudo apt-get update`

### wiringpi
```
sudo apt-get install wiringpi
sudo pip install python-wiringpi
```

### scipy module
`sudo apt-get install python-scipy`

## Find Servo Range (GPIO Example)
We need to determine what the actual range of the servo is. RPi.GPIO accepts percentanges as a duty cycle. Since all servo's are different we need to test to see where the percentages start and stop. Run the following in a terminal session to find this range.

In a terminal run `sudo python` and then paste the following in.
```
import RPi.GPIO as GPIO
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 50)
servo.start(0)
```

Now enter `servo.ChangeDutyCycle(x)` into the console. Keep increasing `x` from 1 - 15 in increments of 1. Watch for when the servo starts moving. If it moves, go back a number and try that, if it moves back, use that number. You can probably jump to 10 or so, and then keep going up till the servo stops. Once it stops, go back by 1, and check to see if it stopped there or on the previous one. What we are looking for is exactly the number the servo starts and stops on. Once you find these numbers make note of them. 

### Update gpio-example.py with new range.
Open the gpio-example.py in your favorite editor, find the line that starts with `dc_range`. Replace the `2` with the lower number that you found. Replace the `13` with the higher number that you found. Likely it will be `[2,13]` if you are using the same servo's that I am here. 


## Find Servo Range (WiringPI Example)
We need to determine what the actual range of the servo is. The specs for the SG90 servo that we used in the video show that the pulse width range is 1ms to 2ms. That would translate in wiringpi to 100 to 200. When I tested that, the range was only 90 degrees of the 180 degree servo. Follow this guide to figure out what the actual pulse width range of your servo is.

Note: You must install wiringpi first

### Setup wiring pi for PWM
```
gpio -g mode 18 pwm
gpio pwm-ms
gpio pwmc 192
gpio pwmr 2000
```


### Find lower range limit
To find the lower range, run the following command replacing 'xx' with a range of 30-100 incrementing by 10's. Watch the servo and see where it starts to move. Once it moves, try -10 from the number that made it move. If it does not move at that number, go back to where you last saw it move. Thats the number you want, keep track of it.

`gpio -g pwm 18 xx`

#### Example
```
gpio -g pwm 18 30
gpio -g pwm 18 40
gpio -g pwm 18 50
...
```

### Find the upper range limit
Follow the same procedure as the lower range, but use a range of 190-270 instead of 30-100, again incrementing in 10's. .  Keep track of the number you find here. 


## Update wiringpi-example.py with new found range. 
Open the `wiringpi-example.py` file in your favorite editor and find the line that starts with `pw_range`. Replace the '50' with the lower number you found, and replace 260 with the higher number you found. 

The script should now be calibrated for the full range of your servo.
