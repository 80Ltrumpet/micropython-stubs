"""
control of WS2812 / NeoPixel LEDs. See: https://docs.micropython.org/en/v1.19.1/library/neopixel.html

This module provides a driver for WS2818 / NeoPixel LEDs.

``Note:`` This module is only included by default on the ESP8266 and ESP32
   ports. On STM32 / Pyboard, you can `download the module
   <https://github.com/micropython/micropython/blob/master/drivers/neopixel/neopixel.py>`_
   and copy it to the filesystem.
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


def bitstream(*args, **kwargs) -> Any:
    ...


class NeoPixel:
    """
    Construct an NeoPixel object.  The parameters are:

        - *pin* is a machine.Pin instance.
        - *n* is the number of LEDs in the strip.
        - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
        - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
    """

    def __init__(self, pin, n, *, bpp=3, timing=1) -> None:
        """"""
        ...

    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        ...

    def fill(self, pixel) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        ...

    ORDER = ()  # type: tuple
