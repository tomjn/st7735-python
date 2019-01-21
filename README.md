# Python ST7735

[![Build Status](https://travis-ci.com/pimoroni/st7735-python.svg?branch=master)](https://travis-ci.com/pimoroni/st7735-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/st7735-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/st7735-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/st7735.svg)](https://pypi.python.org/pypi/st7735)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7735.svg)](https://pypi.python.org/pypi/st7735)


Python library to control an ST7735 TFT LCD display.  Allows simple drawing on the display without installing a kernel module.

Designed specifically to work with a ST7735 based 160x80 pixel TFT SPI display. (Specifically the 0.96" SPI LCD from Pimoroni).

Make sure you have the following dependencies:

````
sudo apt-get update
sudo apt-get install python-rpi.gpio python-spidev python-pip python-imaging python-numpy
````

Install this library by running:

````
sudo pip install st7735
````

See example of usage in the examples folder.

Pimoroni invests time and resources forking and slightly modifying this open source code, please support Pimoroni and open-source software by purchasing products from us, too!

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Modified from 'Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries.' written by Clement Skau.

MIT license, all text above must be included in any redistribution
