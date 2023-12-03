def line_generator(filename: str):
    with open(filename) as file:
        for line in file:
            yield line.strip()


def check(actual: int, expected: int) -> None:
    assert actual == expected, f'Expected {expected} but got {actual}'
