from timeit import timeit
from guppy import hpy

from task_2.array_circular_buffer import ArrayCircularBuffer
from task_2.list_circular_buffer import ListCircularBuffer


def run_task_2_benchmarks(number_of_iterations: int) -> None:
    print(
        timeit(
            "cb.push(1);cb.push(1);cb.push(1);cb.push(1);cb.push(1);cb.pop();cb.pop();cb.pop();cb.pop();cb.pop()",
            setup="from task_2.list_circular_buffer import ListCircularBuffer;cb=ListCircularBuffer(5)",
            number=number_of_iterations,
        )
    )
    print(
        timeit(
            "cb.push(1);cb.push(1);cb.push(1);cb.push(1);cb.push(1);cb.pop();cb.pop();cb.pop();cb.pop();cb.pop()",
            setup="from task_2.array_circular_buffer import ArrayCircularBuffer;cb=ArrayCircularBuffer(5, 'L')",
            number=number_of_iterations,
        )
    )


def memory_profile_list() -> None:
    queue = ListCircularBuffer(10000)

    for i in range(5000):
        queue.push(i)

    for i in range(2000):
        queue.pop()

    print(hpy().heap())


def memory_profile_array() -> None:
    queue = ArrayCircularBuffer(10000, "L")

    for i in range(5000):
        queue.push(i)

    for i in range(2000):
        queue.pop()

    print(hpy().heap())


def run_memory_profiler():
    memory_profile_list()
    memory_profile_array()
