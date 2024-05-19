from time import sleep
from pynq.overlays.base import BaseOverlay

base = BaseOverlay("base.bit")

Gecikme1 = 0.3
Gecikme2 = 0.1
renk = 0
rgbled_position = [4, 5]

for led in base.leds:
    led.on()

while (base.buttons[3].read() == 0):
    if (base.buttons[0].read() == 1):
        renk = (renk + 1) % 8
        for led in rgbled_position:
            base.rgbleds[led].write(renk)
            base.rgbleds[led].write(renk)
        sleep(Gecikme1)

    elif (base.buttons[1].read() == 1):
        for led in base.leds:
            led.off()
        sleep(Gecikme2)
        for led in base.leds:
            led.toggle()
        sleep(Gecikme2)

    elif (base.buttons[2].read() == 1):
        for led in reversed(base.leds):
            led.off()
        sleep(Gecikme2)
        for led in reversed(base.leds):
            led.toggle()
        sleep(Gecikme2)

print('Uygulama sonlandırıldı ...')
for led in base.leds:
    led.off()

for led in rgbled_position:
    base.rgbleds[led].off()