from timeit import timeit


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
