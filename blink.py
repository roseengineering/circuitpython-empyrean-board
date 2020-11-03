import board
import digitalio
import time

# The User LED on the Empyrean is connected to D13

led_port = board.D13   
led = digitalio.DigitalInOut(led_port)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

