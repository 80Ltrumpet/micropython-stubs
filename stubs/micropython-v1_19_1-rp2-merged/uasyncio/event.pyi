from typing import Any

class Event:
    def __init__(self, *argv, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def set(self, *args, **kwargs) -> Any: ...
    wait: Any
    def is_set(self, *args, **kwargs) -> Any: ...

class ThreadSafeFlag:
    def __init__(self, *argv, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def set(self, *args, **kwargs) -> Any: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    wait: Any
