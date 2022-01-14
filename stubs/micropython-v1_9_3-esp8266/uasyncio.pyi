from typing import Any

DEBUG: int

class EventLoop:
    def call_at_(self, *argv) -> Any: ...
    def call_later(self, *argv) -> Any: ...
    def call_later_ms(self, *argv) -> Any: ...
    def call_soon(self, *argv) -> Any: ...
    def close(self, *argv) -> Any: ...
    def create_task(self, *argv) -> Any: ...
    def run_forever(self, *argv) -> Any: ...
    def run_until_complete(self, *argv) -> Any: ...
    def stop(self, *argv) -> Any: ...
    def time(self, *argv) -> Any: ...
    def wait(self, *argv) -> Any: ...

class IORead: ...
class IOReadDone: ...
class IOWrite: ...
class IOWriteDone: ...

class PollEventLoop:
    def add_reader(self, *argv) -> Any: ...
    def add_writer(self, *argv) -> Any: ...
    def remove_reader(self, *argv) -> Any: ...
    def remove_writer(self, *argv) -> Any: ...
    def wait(self, *argv) -> Any: ...

class SleepMs: ...
class StopLoop: ...

class StreamReader:
    aclose: Any
    read: Any
    readexactly: Any
    readline: Any

class StreamWriter:
    aclose: Any
    awrite: Any
    awriteiter: Any
    def get_extra_info(self, *argv) -> Any: ...

class SysCall:
    def handle(self, *argv) -> Any: ...

class SysCall1: ...

def Task() -> None: ...

_socket: Any
core: Any

def coroutine() -> None: ...
def ensure_future() -> None: ...
def get_event_loop() -> None: ...

log: Any
open_connection: Any
select: Any

def set_debug() -> None: ...

sleep: Any
sleep_ms: Any
start_server: Any
time: Any

class type_gen:
    def close(self, *argv) -> Any: ...
    def send(self, *argv) -> Any: ...
    def throw(self, *argv) -> Any: ...

uasyncio: Any
uerrno: Any
utimeq: Any
