"""
mathematical functions. See: https://docs.micropython.org/en/v1.17/library/math.html

|see_cpython_module| :mod:`python:math` https://docs.python.org/3/library/math.html .

The ``math`` module provides some basic mathematical functions for
working with floating-point numbers.

*Note:* On the pyboard, floating-point numbers have 32-bit precision.

Availability: not available on WiPy. Floating point support required
for this module.
"""
from typing import Callable, Coroutine, Dict, Generator, IO, Iterator, List, NoReturn, Optional, Tuple, Union, Any

def pow(x, y) -> Any:
    """
    Returns ``x`` to the power of ``y``.
    """
    ...
def acos(x) -> float:
    """
    Return the inverse cosine of ``x``.
    """
    ...
def asin(x) -> float:
    """
    Return the inverse sine of ``x``.
    """
    ...
def atan(x) -> float:
    """
    Return the inverse tangent of ``x``.
    """
    ...
def atan2(y, x) -> float:
    """
    Return the principal value of the inverse tangent of ``y/x``.
    """
    ...
def ceil(x) -> int:
    """
    Return an integer, being ``x`` rounded towards positive infinity.
    """
    ...
def copysign(x, y) -> Any:
    """
    Return ``x`` with the sign of ``y``.
    """
    ...
def cos(x) -> float:
    """
    Return the cosine of ``x``.
    """
    ...
def degrees(x) -> Any:
    """
    Return radians ``x`` converted to degrees.
    """
    ...

e: float

def exp(x) -> float:
    """
    Return the exponential of ``x``.
    """
    ...
def fabs(x) -> Any:
    """
    Return the absolute value of ``x``.
    """
    ...
def floor(x) -> int:
    """
    Return an integer, being ``x`` rounded towards negative infinity.
    """
    ...
def fmod(x, y) -> Any:
    """
    Return the remainder of ``x/y``.
    """
    ...
def frexp(x) -> Any:
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
    exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
    the relation ``0.5 <= abs(m) < 1`` holds.
    """
    ...
def isfinite(x) -> bool:
    """
    Return ``True`` if ``x`` is finite.
    """
    ...
def isinf(x) -> bool:
    """
    Return ``True`` if ``x`` is infinite.
    """
    ...
def isnan(x) -> bool:
    """
    Return ``True`` if ``x`` is not-a-number
    """
    ...
def ldexp(x, exp) -> Any:
    """
    Return ``x * (2**exp)``.
    """
    ...
def log(x) -> float:
    """
    Return the natural logarithm of ``x``.
    """
    ...
def modf(x) -> Tuple:
    """
    Return a tuple of two floats, being the fractional and integral parts of
    ``x``.  Both return values have the same sign as ``x``.
    """
    ...

pi: float

def radians(x) -> Any:
    """
    Return degrees ``x`` converted to radians.
    """
    ...
def sin(x) -> float:
    """
    Return the sine of ``x``.
    """
    ...
def sqrt(x) -> Any:
    """
    Return the square root of ``x``.
    """
    ...
def tan(x) -> float:
    """
    Return the tangent of ``x``.
    """
    ...
def trunc(x) -> int:
    """
    Return an integer, being ``x`` rounded towards 0.
    """
    ...
