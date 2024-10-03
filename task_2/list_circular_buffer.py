from typing import TypeVar, Generic, cast
from .exceptions_ import (
    BufferIsEmptyError,
    BufferIsFullError,
    BufferIncorrectSizeError,
)

T = TypeVar("T")


class _EmptyValue:
    __slots__ = ()


class ListCircularBuffer(Generic[T]):
    """
    List based circular buffer implementation
    """

    def __init__(self, size: int) -> None:
        """Constructor of list circular buffer

        Args:
            size (int): size of the circular buffer

        Raises:
            BufferIncorrectSizeError: incorrect size exception
        """
        self._validate_size(size)

        self._queue: list[_EmptyValue | T] = [_EmptyValue() for _ in range(size)]
        self._head = 0
        self._tail = 0
        self._size = size

    def push(self, value: T) -> None:
        """Push value into the circular buffer

        Args:
            value (T): value to push

        Raises:
            BufferIsFullError: raised if buffer is full
        """
        if self._is_full():
            raise BufferIsFullError("Buffer is full")

        self._queue[self._tail] = value
        self._increment_tail()

    def pop(self) -> T:
        """Pull value from the circular buffer

        Raises:
            BufferIsEmptyError: raised if there is nothing to pull

        Returns:
            T: pulled value
        """
        if self._is_empty():
            raise BufferIsEmptyError("Buffer is empty")

        value: _EmptyValue | T = self._queue[self._head]
        value = cast(T, value)

        self._queue[self._head] = _EmptyValue()
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
        return isinstance(self._queue[self._head], _EmptyValue)

    def _is_full(self) -> bool:
        return not isinstance(self._queue[self._tail], _EmptyValue)
