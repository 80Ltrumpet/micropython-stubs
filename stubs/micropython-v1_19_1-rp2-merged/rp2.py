"""
functionality specific to the RP2. See: https://docs.micropython.org/en/v1.19.1/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.

"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.7.2
from typing import Any, Optional


def const(*args, **kwargs) -> Any:
    ...


class Flash:
    """
    Gets the singleton object for accessing the SPI flash memory.

    """

    def __init__(self) -> None:
        ...

    def ioctl(self, cmd, arg) -> Any:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`os.AbstractBlockDev`.
        """
        ...

    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> Any:
        ...

    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> Any:
        ...


class PIO:
    """
    Gets the PIO instance numbered *id*. The RP2040 has two PIO instances,
    numbered 0 and 1.

    Raises a ``ValueError`` if any other argument is provided.

    """

    def __init__(self, id) -> None:
        ...

    IN_HIGH = 1  # type: int
    IN_LOW = 0  # type: int
    IRQ_SM0 = 256  # type: int
    IRQ_SM1 = 512  # type: int
    IRQ_SM2 = 1024  # type: int
    IRQ_SM3 = 2048  # type: int
    JOIN_NONE = 0  # type: int
    JOIN_RX = 2  # type: int
    JOIN_TX = 1  # type: int
    OUT_HIGH = 3  # type: int
    OUT_LOW = 2  # type: int
    SHIFT_LEFT = 0  # type: int
    SHIFT_RIGHT = 1  # type: int

    def add_program(self, program) -> Any:
        """
        Add the *program* to the instruction memory of this PIO instance.

        The amount of memory available for programs on each PIO instance is
        limited. If there isn't enough space left in the PIO's program memory
        this method will raise ``OSError(ENOMEM)``.
        """
        ...

    def irq(self, handler=None, trigger=IRQ_SM0, hard=False) -> Any:
        """
        Returns the IRQ object for this PIO instance.

        MicroPython only uses IRQ 0 on each PIO instance. IRQ 1 is not available.

        Optionally configure it.

        """
        ...

    def remove_program(self, program: Optional[Any] = None) -> None:
        """
        Remove *program* from the instruction memory of this PIO instance.

        If no program is provided, it removes all programs.

        It is not an error to remove a program which has already been removed.
        """
        ...

    def state_machine(self, id, program, *args: Optional[Any]) -> Any:
        """
        Gets the state machine numbered *id*. On the RP2040, each PIO instance has
        four state machines, numbered 0 to 3.

        Optionally initialize it with a *program*: see `StateMachine.init`.

        >>> rp2.PIO(1).state_machine(3)
        StateMachine(7)
        """
        ...


class StateMachine:
    """
    Get the state machine numbered *id*. The RP2040 has two identical PIO
    instances, each with 4 state machines: so there are 8 state machines in
    total, numbered 0 to 7.

    Optionally initialize it with the given program *program*: see
    `StateMachine.init`.

    """

    def __init__(self, id, program, *args: Optional[Any]) -> None:
        ...

    def exec(self, instr) -> Any:
        """
        Execute a single PIO instruction. Uses `asm_pio_encode` to encode the
        instruction from the given string *instr*.

        >>> sm.exec("set(0, 1)")
        """
        ...

    def get(self, buf=None, shift=0) -> Any:
        """
        Pull a word from the state machine's RX FIFO.

        If the FIFO is empty, it blocks until data arrives (i.e. the state machine
        pushes a word).

        The value is shifted right by *shift* bits before returning, i.e. the
        return value is ``word >> shift``.
        """
        ...

    def active(self, value: Optional[Any] = None) -> Any:
        """
        Gets or sets whether the state machine is currently running.

        >>> sm.active()
        True
        >>> sm.active(0)
        False
        """
        ...

    def init(
        self,
        program,
        freq=-1,
        *,
        in_base=None,
        out_base=None,
        set_base=None,
        jmp_pin=None,
        sideset_base=None,
        in_shiftdir=None,
        out_shiftdir=None,
        push_thresh=None,
        pull_thresh=None,
    ) -> None:
        """
        Configure the state machine instance to run the given *program*.

        The program is added to the instruction memory of this PIO instance. If the
        instruction memory already contains this program, then its offset is
        re-used so as to save on instruction memory.

        - *freq* is the frequency in Hz to run the state machine at. Defaults to
          the system clock frequency.

          The clock divider is computed as ``system clock frequency / freq``, so
          there can be slight rounding errors.

          The minimum possible clock divider is one 65536th of the system clock: so
          at the default system clock frequency of 125MHz, the minimum value of
          *freq* is ``1908``. To run state machines at slower frequencies, you'll
          need to reduce the system clock speed with `machine.freq()`.
        - *in_base* is the first pin to use for ``in()`` instructions.
        - *out_base* is the first pin to use for ``out()`` instructions.
        - *set_base* is the first pin to use for ``set()`` instructions.
        - *jmp_pin* is the first pin to use for ``jmp(pin, ...)`` instructions.
        - *sideset_base* is the first pin to use for side-setting.
        - *in_shiftdir* is the direction the ISR will shift, either
          `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
        - *out_shiftdir* is the direction the OSR will shift, either
          `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
        - *push_thresh* is the threshold in bits before auto-push or conditional
          re-pushing is triggered.
        - *pull_thresh* is the threshold in bits before auto-push or conditional
          re-pushing is triggered.
        """
        ...

    def irq(self, handler=None, trigger=0 | 1, hard=False) -> Any:
        """
        Returns the IRQ object for the given StateMachine.

        Optionally configure it.
        """
        ...

    def put(self, value, shift=0) -> Any:
        """
        Push a word onto the state machine's TX FIFO.

        If the FIFO is full, it blocks until there is space (i.e. the state machine
        pulls a word).

        The value is first shifted left by *shift* bits, i.e. the state machine
        receives ``value << shift``.
        """
        ...

    def restart(self) -> Any:
        """
        Restarts the state machine and jumps to the beginning of the program.

        This method clears the state machine's internal state using the RP2040's
        ``SM_RESTART`` register. This includes:

         - input and output shift counters
         - the contents of the input shift register
         - the delay counter
         - the waiting-on-IRQ state
         - a stalled instruction run using `StateMachine.exec()`
        """
        ...

    def rx_fifo(self) -> int:
        """
        Returns the number of words in the state machine's RX FIFO. A value of 0
        indicates the FIFO is empty.

        Useful for checking if data is waiting to be read, before calling
        `StateMachine.get()`.
        """
        ...

    def tx_fifo(self) -> int:
        """
        Returns the number of words in the state machine's TX FIFO. A value of 0
        indicates the FIFO is empty.

        Useful for checking if there is space to push another word using
        `StateMachine.put()`.
        """
        ...


def asm_pio_encode(instr, sideset_count, sideset_opt=False) -> Any:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """
    ...


def country(*args, **kwargs) -> Any:
    ...


def dht_readinto(*args, **kwargs) -> Any:
    ...


class PIOASMError(Exception):
    """
    This exception is raised from `asm_pio()` or `asm_pio_encode()` if there is
    an error assembling a PIO program.

    """

    ...


class PIOASMEmit:
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def label(self, *args, **kwargs) -> Any:
        ...

    def mov(self, *args, **kwargs) -> Any:
        ...

    def nop(self, *args, **kwargs) -> Any:
        ...

    def pull(self, *args, **kwargs) -> Any:
        ...

    def push(self, *args, **kwargs) -> Any:
        ...

    def wrap_target(self, *args, **kwargs) -> Any:
        ...

    def wrap(self, *args, **kwargs) -> Any:
        ...

    def word(self, *args, **kwargs) -> Any:
        ...

    def jmp(self, *args, **kwargs) -> Any:
        ...

    def wait(self, *args, **kwargs) -> Any:
        ...

    def in_(self, *args, **kwargs) -> Any:
        ...

    def out(self, *args, **kwargs) -> Any:
        ...

    def start_pass(self, *args, **kwargs) -> Any:
        ...

    def delay(self, *args, **kwargs) -> Any:
        ...

    def side(self, *args, **kwargs) -> Any:
        ...


def asm_pio(
    *,
    out_init=None,
    set_init=None,
    sideset_init=None,
    in_shiftdir=0,
    out_shiftdir=0,
    autopush=False,
    autopull=False,
    push_thresh=32,
    pull_thresh=32,
    fifo_join=PIO.JOIN_NONE,
) -> Any:
    """
    Assemble a PIO program.

    The following parameters control the initial state of the GPIO pins, as one
    of `PIO.IN_LOW`, `PIO.IN_HIGH`, `PIO.OUT_LOW` or `PIO.OUT_HIGH`. If the
    program uses more than one pin, provide a tuple, e.g.
    ``out_init=(PIO.OUT_LOW, PIO.OUT_LOW)``.

    - *out_init* configures the pins used for ``out()`` instructions.
    - *set_init* configures the pins used for ``set()`` instructions. There can
      be at most 5.
    - *sideset_init* configures the pins used side-setting. There can be at
      most 5.

    The following parameters are used by default, but can be overridden in
    `StateMachine.init()`:

    - *in_shiftdir* is the default direction the ISR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *out_shiftdir* is the default direction the OSR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *push_thresh* is the threshold in bits before auto-push or conditional
      re-pushing is triggered.
    - *pull_thresh* is the threshold in bits before auto-push or conditional
      re-pushing is triggered.

    The remaining parameters are:

    - *autopush* configures whether auto-push is enabled.
    - *autopull* configures whether auto-pull is enabled.
    - *fifo_join* configures whether the 4-word TX and RX FIFOs should be
      combined into a single 8-word FIFO for one direction only. The options
      are `PIO.JOIN_NONE`, `PIO.JOIN_RX` and `PIO.JOIN_TX`.
    """
    ...
