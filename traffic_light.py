from gpiozero import LED
from time import sleep

red = LED(4)
amber = LED(17)
green = LED(27)

green.on()
amber.off()
red.off()

while True:
    sleep(5)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(5)
    green.on()
    amber.off()
    red.off()