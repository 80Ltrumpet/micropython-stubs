from typing import Any

class OneWire:
    MATCH_ROM: int
    SEARCH_ROM: int
    SKIP_ROM: int
    def _search_rom(self, *args) -> Any: ...
    def crc8(self, *args) -> Any: ...
    def readbit(self, *args) -> Any: ...
    def readbyte(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def reset(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def select_rom(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def writebit(self, *args) -> Any: ...
    def writebyte(self, *args) -> Any: ...

class OneWireError: ...

_ow: Any
