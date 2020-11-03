
print(f"""\

This repo contains an experimental Circuitpython implementation
for the Empyrean board, specifically the Empyrean alpha version
of the board.

Circuitpython is located on github here:
https://github.com/adafruit/circuitpython

The Empyrean board and its documenation are located at
https://www.etherkit.com/microcontrollers/empyrean.html
The board uses the ATSAMD21 ARM MCU.

To create the implementation I first copied one of the existing
Circuitpython boards located under
the circuitpython/ports/atmel-samd/boards
directory as a template.  Since the Empyrean does not use an external
flash, I used the sparkfun_samd21_mini board which has no
external flash and used the same MCU.

I modified the pin mapping
located in the pins.c file to conform to the Empyrean schematic.
The file mpconfigboard.c also contains a few pin mappings.
In it, I remapped the I2C pins.  The rest of the pins were unchanged.  The Empyrean
board name and MCU name were set in files mpconfigboard.mk and mpconfigboard.h.
The mpconfigboard.mk file contained additional settings
like USB vendor and product id.  In it, I configured
the implementation to use an internal flash, a small build, no
long integers, and no gcc -O3 optimization.

I used the following script located in empyrean-alpha.sh
to build the board's firmware.uf2 file.  Make sure your
computer's version of gcc is not version 10 because
it breaks the cross compilation phase. I recommend gcc version 8.

```bash
{open("empyrean-alpha.sh").read()}```

To test the board, copy over blink.py as main.py into Empyrean's CIRCUITPY 
drive.

""")

