def is_even_bitwise(value: int) -> bool:
    return value & 1 == 0


def is_even_classic(value: int) -> bool:
    return value % 2 == 0
