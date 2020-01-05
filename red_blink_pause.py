from gpiozero import LED
from time import sleep
from signal import pause

red = LED(17)

red.blink(1, 1)
pause()