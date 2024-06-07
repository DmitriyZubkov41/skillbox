#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

m = MediumMotor('outD')
m.run_timed(time_sp=1000, speed_sp=650)

sleep(4)