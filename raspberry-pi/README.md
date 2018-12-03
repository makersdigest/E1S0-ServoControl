# Maker's Digest
## Raspberry Pi Servo Control

## Installation
The wiringpi-complete.py example requires that software be installed on your pi.

`sudo apt-get update`

### wiringpi
`sudo apt-get install wiringpi`

`sudo pip install python-wiringpi`

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


### Find lower range
`gpio -g pwm 18 50`

