from __future__ import division
from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause

cpu = CPUTemperature(min_temp=50, max_temp=90)
leds = LEDBarGraph(17, 4, pwm=True)

leds.source = cpu

pause()