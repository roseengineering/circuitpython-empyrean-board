
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
like USB vendor and product id.  In it I configured
the implementation to use an internal flash, a small build, no
long integers, and no gcc -O3 optimization.

I used the following script located in empyrean-alpha.sh
to build the board's firmware.uf2 file.  Make sure your
computer's version of gcc is not version 10 because
it breaks the cross compilation phase. I recommend gcc version 8.

```bash
curl -LO https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2
sudo tar xf gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2 -C /usr/local --no-same-owner
PATH="/usr/local/gcc-arm-none-eabi-9-2019-q4-major/bin:$PATH"
sudo apt-get install -y build-essential  # make sure gcc-8 not gcc-10
sudo apt-get install -y gettext
git clone https://github.com/adafruit/circuitpython
cp -r empyrean-alpha circuitpython/ports/atmel-samd/boards
cd circuitpython/
git checkout tags/5.3.1
git submodule sync
git submodule update --init
make -C mpy-cross 
cd ports/atmel-samd/
make BOARD=empyrean-alpha
```

To test the board, copy blink.py as main.py into Empyrean's CIRCUITPY 
drive.


