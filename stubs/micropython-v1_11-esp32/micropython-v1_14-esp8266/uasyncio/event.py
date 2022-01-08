"""
Module: 'uasyncio.event' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


class Event:
    """"""

    def __init__(self, *args) -> None:
        ...

    def clear(self, *args) -> Any:
        ...

    def set(self, *args) -> Any:
        ...

    def is_set(self, *args) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>
