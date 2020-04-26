#!/usr/bin/env python3.7
import Adafruit_PCA9685
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-s", default=6, help="servo", type=int)
parser.add_argument("-p", default=300, help="position of servo", type=int)
parser.add_argument("-g", help="go", type=bool)
args = parser.parse_args()
servo = args.s
position = args.p

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

if args.g:
    # 0
    pwm.set_pwm(6,0,300)
    pwm.set_pwm(7,0,300)
    # 1
    pwm.set_pwm(6,0,300)
    pwm.set_pwm(7,0,210)
    time.sleep(0.5)
    # 2
    pwm.set_pwm(6,0,335)
    pwm.set_pwm(7,0,330)
    time.sleep(0.5)
    # 3
    pwm.set_pwm(6,0,300)
    pwm.set_pwm(7,0,330)
    time.sleep(0.5)
    # 4
    pwm.set_pwm(6,0,270)
    pwm.set_pwm(7,0,330)
    time.sleep(0.5)
    # 5 end
    #pwm.set_pwm(6,0,300)
    #pwm.set_pwm(7,0,300)
else:
    pwm.set_pwm(servo,0,position)
