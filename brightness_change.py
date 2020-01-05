from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.3  # 0.3 almost half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)