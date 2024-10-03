from timeit import timeit


def run_task_1_benchmarks(number_of_iterations: int) -> None:
    print(
        timeit(
            "is_even_classic(10002)",
            setup="from task_1.main import is_even_classic",
            number=number_of_iterations,
        )
    )
    print(
        timeit(
            "is_even_bitwise(10002)",
            setup="from task_1.main import is_even_bitwise",
            number=number_of_iterations,
        )
    )
