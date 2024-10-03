import pytest
from task_2.array_circular_buffer import ArrayCircularBuffer
from task_2.exceptions_ import (
    BufferIsEmptyError,
    BufferIsFullError,
    BufferIncorrectSizeError,
)


def test_list_circular_buffer_push_pop():
    """Normal usage"""
    queue = ArrayCircularBuffer(5, "L")
    queue.push(12)
    assert queue.pop() == 12, "Incorrect value was pulled out from list circular buffer"

    queue.push(41)
    queue.push(42)
    queue.push(43)
    queue.push(44)
    queue.push(45)

    assert queue.pop() == 41, "Incorrect value was pulled out from list circular buffer"
    assert queue.pop() == 42, "Incorrect value was pulled out from list circular buffer"
    assert queue.pop() == 43, "Incorrect value was pulled out from list circular buffer"
    assert queue.pop() == 44, "Incorrect value was pulled out from list circular buffer"
    assert queue.pop() == 45, "Incorrect value was pulled out from list circular buffer"

    queue.push(777)
    queue.push(778)
    queue.push(779)
    queue.push(780)

    assert (
        queue.pop() == 777
    ), "Incorrect value was pulled out from list circular buffer"
    assert (
        queue.pop() == 778
    ), "Incorrect value was pulled out from list circular buffer"
    assert (
        queue.pop() == 779
    ), "Incorrect value was pulled out from list circular buffer"
    assert (
        queue.pop() == 780
    ), "Incorrect value was pulled out from list circular buffer"


@pytest.mark.parametrize("input_size", [(0), (-1), (-100)])
def test_list_circular_buffer_raises_incorrect_size(input_size):
    with pytest.raises(BufferIncorrectSizeError):
        ArrayCircularBuffer(input_size, "L")


def test_list_circular_buffer_raises_buffer_is_empty_when_initialized():
    queue = ArrayCircularBuffer(5, "L")

    with pytest.raises(BufferIsEmptyError):
        queue.pop()


def test_list_circular_buffer_raises_buffer_is_empty_when_all_values_pulled():
    queue = ArrayCircularBuffer(5, "L")

    queue.push(1)
    queue.push(2)
    queue.push(3)

    queue.pop()
    queue.pop()
    queue.pop()

    with pytest.raises(BufferIsEmptyError):
        queue.pop()


def test_list_circular_buffer_raises_buffer_is_full():
    queue = ArrayCircularBuffer(3, "L")

    queue.push(1)
    queue.push(2)
    queue.push(3)

    with pytest.raises(BufferIsFullError):
        queue.push(4)
