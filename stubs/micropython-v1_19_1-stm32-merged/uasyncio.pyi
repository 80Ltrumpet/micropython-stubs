from typing import Any

class CancelledError(Exception): ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...

class TaskQueue:
    def __init__(self, *argv, **kwargs) -> None: ...
    def pop(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def peek(self, *args, **kwargs) -> Any: ...
    def push(self, *args, **kwargs) -> Any: ...

def sleep(*args, **kwargs) -> Any: ...
def sleep_ms(*args, **kwargs) -> Any: ...
def ticks_add(*args, **kwargs) -> Any: ...
def ticks_diff(*args, **kwargs) -> Any: ...

wait_for: Any
gather: Any

class Event:
    def __init__(self, *argv, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def set(self, *args, **kwargs) -> Any: ...
    def is_set(self, *args, **kwargs) -> Any: ...
    wait: Any

class Lock:
    def __init__(self, *argv, **kwargs) -> None: ...
    def release(self, *args, **kwargs) -> Any: ...
    def locked(self, *args, **kwargs) -> Any: ...
    acquire: Any

def wait_for_ms(*args, **kwargs) -> Any: ...

class ThreadSafeFlag:
    def __init__(self, *argv, **kwargs) -> None: ...
    def set(self, *args, **kwargs) -> Any: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    wait: Any

open_connection: Any
start_server: Any

class StreamReader:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args, **kwargs) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    drain: Any
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    readexactly: Any

class StreamWriter:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    read: Any
    readinto: Any
    readline: Any
    def write(self, *args, **kwargs) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    drain: Any
    def get_extra_info(self, *args, **kwargs) -> Any: ...
    readexactly: Any

class TimeoutError(Exception): ...

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

class IOQueue:
    def __init__(self, *argv, **kwargs) -> None: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def wait_io_event(self, *args, **kwargs) -> Any: ...
    def queue_read(self, *args, **kwargs) -> Any: ...
    def queue_write(self, *args, **kwargs) -> Any: ...

class Loop:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args, **kwargs) -> Any: ...
    def stop(self, *args, **kwargs) -> Any: ...
    def create_task(self, *args, **kwargs) -> Any: ...
    def run_until_complete(self, *args, **kwargs) -> Any: ...
    def call_exception_handler(self, *args, **kwargs) -> Any: ...
    def run_forever(self, *args, **kwargs) -> Any: ...
    def set_exception_handler(self, *args, **kwargs) -> Any: ...
    def get_exception_handler(self, *args, **kwargs) -> Any: ...
    def default_exception_handler(self, *args, **kwargs) -> Any: ...

def create_task(*args, **kwargs) -> Any: ...
def run_until_complete(*args, **kwargs) -> Any: ...
def run(*args, **kwargs) -> Any: ...
def get_event_loop(*args, **kwargs) -> Any: ...
def current_task(*args, **kwargs) -> Any: ...
def new_event_loop(*args, **kwargs) -> Any: ...
def ticks(*args, **kwargs) -> Any: ...
