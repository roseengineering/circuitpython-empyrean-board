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
