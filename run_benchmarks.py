from argparse import ArgumentParser
from tests.test_task_1.benchmarks import run_task_1_benchmarks
from tests.test_task_2.benchmarks import run_task_2_benchmarks


def _initialize_argparser() -> ArgumentParser:
    parser = ArgumentParser(description="Run task benchmarks")

    parser.add_argument(
        "-t", "--task", type=int, help="Task Number", choices=[1, 2], required=True
    )
    parser.add_argument(
        "-i", "--iterations", type=int, help="Number of iterations", required=True
    )

    return parser


def main():
    argparser = _initialize_argparser()
    args = argparser.parse_args()

    match args.task:
        case 1:
            run_task_1_benchmarks(args.iterations)
        case 2:
            run_task_2_benchmarks(args.iterations)


if __name__ == "__main__":
    main()
