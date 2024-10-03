from task_2.array_circular_buffer import ArrayCircularBuffer
from task_2.list_circular_buffer import ListCircularBuffer
from guppy import hpy


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


if __name__ == "__main__":
    run_memory_profiler()
