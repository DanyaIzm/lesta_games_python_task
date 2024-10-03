from typing import Literal, Type, TypeAlias, TypeVar, Generic, cast
from array import array
from .exceptions_ import (
    BufferIsEmptyError,
    BufferIsFullError,
    BufferIncorrectSizeError,
)

# https://docs.python.org/3/library/array.html
_IntTypeCode: TypeAlias = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode: TypeAlias = Literal["f", "d"]
_UnicodeTypeCode: TypeAlias = Literal["u"]
_TypeCode: TypeAlias = _IntTypeCode | _FloatTypeCode | _UnicodeTypeCode

T = TypeVar("T", int, float, str)


class _EmptyValue:
    __slots__ = ()


class ArrayCircularBuffer(Generic[T]):
    """
    array.array based circular buffer implementation
    """

    def __init__(self, size: int, type: _TypeCode) -> None:
        """Constructor of array circular buffer

        Args:
            size (int): size of the circular buffer
            type (_TypeCode): array.array typecode

        Raises:
            BufferIncorrectSizeError: incorrect size exception
        """
        self._validate_size(size)

        self._queue = array(type)
        self._queue.fromlist([0 for _ in range(size)])

        self._empty_full_mapping = array("B")
        self._empty_full_mapping.fromlist([0 for _ in range(size)])

        self._head = 0
        self._tail = 0
        self._size = size

    def push(self, value: T) -> None:
        if self._is_full():
            raise BufferIsFullError("Buffer is full")

        self._queue[self._tail] = value
        self._empty_full_mapping[self._tail] = 1
        self._increment_tail()

    def pop(self) -> T:
        if self._is_empty():
            raise BufferIsEmptyError("Buffer is empty")

        value = self._queue[self._head]

        self._empty_full_mapping[self._head] = 0
        self._increment_head()

        return value

    def _validate_size(self, size: int) -> None:
        """Validates buffer size argument and raises if it is invalid

        Args:
            size (int): client input size of the circular buffer

        Raises:
            BufferIncorrectSizeError: incorrect size exception
        """
        if size <= 0:
            raise BufferIncorrectSizeError(
                f"Invalid circular buffer {size=}. Size must be positive integer."
            )

    def _increment_head(self) -> None:
        self._head = (self._head + 1) % self._size

    def _increment_tail(self) -> None:
        self._tail = (self._tail + 1) % self._size

    def _is_empty(self) -> bool:
        return self._empty_full_mapping[self._head] == 0

    def _is_full(self) -> bool:
        return self._empty_full_mapping[self._tail] == 1
