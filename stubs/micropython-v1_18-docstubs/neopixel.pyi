"""
control of WS2812 / NeoPixel LEDs. See: https://docs.micropython.org/en/v1.18/library/neopixel.html

This module provides a driver for WS2818 / NeoPixel LEDs.

``Note:`` This module is only included by default on the ESP8266 and ESP32
   ports. On STM32 / Pyboard, you can `download the module
   <https://github.com/micropython/micropython/blob/master/drivers/neopixel/neopixel.py>`_
   and copy it to the filesystem.
"""

# source version: v1_18
# origin module:: repos/micropython/docs/library/neopixel.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union

class NeoPixel:
    """
    Construct an NeoPixel object.  The parameters are:

        - *pin* is a machine.Pin instance.
        - *n* is the number of LEDs in the strip.
        - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
        - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
    """

    def __init__(self, pin, n, *, bpp=3, timing=1) -> None: ...
    def fill(self, pixel) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        ...
    def __len__(self) -> int:
        """
        Returns the number of LEDs in the strip.
        """
        ...
    def __setitem__(self, index, val) -> None:
        """
        Set the pixel at *index* to the value, which is an RGB/RGBW tuple.
        """
        ...
    def __getitem__(self, index) -> Tuple:
        """
        Returns the pixel at *index* as an RGB/RGBW tuple.
        """
        ...
    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        ...
