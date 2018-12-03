# Maker's Digest
## Raspberry Pi Servo Control

## Installation
The wiringpi-complete.py example requires that software be installed on your pi.

`sudo apt-get update`

### wiringpi
```
sudo apt-get install wiringpi
sudo pip install python-wiringpi
```

### scipy module
`sudo apt-get install python-scipy`

## Find Servo Range
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
