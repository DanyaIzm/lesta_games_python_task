from timeit import timeit


def run_task_1_benchmarks():
    print(
        timeit(
            "is_even_classic(10002)",
            setup="from task_1.main import is_even_classic",
            number=1_000_000_000,
        )
    )
    print(
        timeit(
            "is_even_bitwise(10002)",
            setup="from task_1.main import is_even_bitwise",
            number=1_000_000_000,
        )
    )
