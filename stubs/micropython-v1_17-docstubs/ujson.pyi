"""
JSON encoding and decoding. See: https://docs.micropython.org/en/v1.17/library/json.html

|see_cpython_module| :mod:`python:json` https://docs.python.org/3/library/json.html .

This modules allows to convert between Python objects and the JSON
data format.
"""

# source version: v1_17
# origin module:: repos/micropython/docs/library/json.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union

def dump(obj, stream, separators=None) -> Any:
    """
    Serialise *obj* to a JSON string, writing it to the given *stream*.

    If specified, separators should be an ``(item_separator, key_separator)``
    tuple. The default is ``(', ', ': ')``. To get the most compact JSON
    representation, you should specify ``(',', ':')`` to eliminate whitespace.
    """
    ...

def dumps(obj, separators=None) -> str:
    """
    Return *obj* represented as a JSON string.

    The arguments have the same meaning as in `dump`.
    """
    ...

def load(stream) -> Any:
    """
    Parse the given *stream*, interpreting it as a JSON string and
    deserialising the data to a Python object.  The resulting object is
    returned.

    Parsing continues until end-of-file is encountered.
    A :exc:`ValueError` is raised if the data in *stream* is not correctly formed.
    """
    ...

def loads(str) -> Any:
    """
    Parse the JSON *str* and return an object.  Raises :exc:`ValueError` if the
    string is not correctly formed.
    """
    ...
