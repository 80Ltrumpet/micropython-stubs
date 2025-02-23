"""
functionality specific to STM32 MCUs. See: https://docs.micropython.org/en/v1.19.1/library/stm.html

This module provides functionality specific to STM32 microcontrollers, including
direct access to peripheral registers.
"""

# + module: stm.rst
# source version: v1_19_1
# origin module:: repos/micropython/docs/library/stm.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union

mem8: bytearray
"""Read/write 8 bits of memory."""
mem16: bytearray
"""Read/write 16 bits of memory."""
mem32: bytearray
"""\
Read/write 32 bits of memory.

Use subscript notation ``[...]`` to index these objects with the address of
interest.

These memory objects can be used in combination with the peripheral register
constants to read and write registers of the MCU hardware peripherals, as well
as all other areas of address space.

"""
GPIOA: int = 1
"""Base address of the GPIOA peripheral."""
GPIOB: int = 1
"""Base address of the GPIOB peripheral."""
GPIO_BSRR: Any = ...
"""Offset of the GPIO bit set/reset register."""
GPIO_IDR: Any = ...
"""Offset of the GPIO input data register."""
GPIO_ODR: int = 1
"""\
Offset of the GPIO output data register.

Constants that are named after a peripheral, like ``GPIOA``, are the absolute
address of that peripheral.  Constants that have a prefix which is the name of a
peripheral, like ``GPIO_BSRR``, are relative offsets of the register.  Accessing
peripheral registers requires adding the absolute base address of the peripheral
and the relative register offset.  For example ``GPIOA + GPIO_BSRR`` is the
full, absolute address of the ``GPIOA->BSRR`` register.

Example use:
"""

def rfcore_status() -> int:
    """
    Returns the status of the second CPU as an integer (the first word of device
    info table).
    """
    ...

def rfcore_fw_version(id) -> Tuple:
    """
    Get the version of the firmware running on the second CPU.  Pass in 0 for
    *id* to get the FUS version, and 1 to get the WS version.

    Returns a 5-tuple with the full version number.
    """
    ...

def rfcore_sys_hci(ogf, ocf, data, timeout_ms=0) -> bytes:
    """
    Execute a HCI command on the SYS channel.  The execution is synchronous.

    Returns a bytes object with the result of the SYS command.
    """
    ...
