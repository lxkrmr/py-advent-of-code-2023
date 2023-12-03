from utils import line_generator, check


def main():
    check(part_one('test_input_part_one.txt'), 142)
    print(part_one('puzzle_input.txt'))

    check(part_two('test_input_part_two.txt'), 281)
    print(part_two('puzzle_input.txt'))


def part_one(filename: str) -> int:
    return sum([
        to_calibration_value(extract_digits_part_one(line))
        for line
        in line_generator(filename)
    ])


def part_two(filename: str) -> int:
    return sum([
        to_calibration_value(extract_digits_part_two(line))
        for line
        in line_generator(filename)
    ])


def extract_digits_part_one(line: str) -> [int]:
    return [int(char) for char in line if char.isdigit()]


def to_calibration_value(digits: [int]):
    result = int(f'{digits[0]}{digits[-1]}')
    print(result, digits)
    return result


PREFIXES_TO_DIGITS = [
    ("1", 1), ("one", 1),
    ("2", 2), ("two", 2),
    ("3", 3), ("three", 3),
    ("4", 4), ("four", 4),
    ("5", 5), ("five", 5),
    ("6", 6), ("six", 6),
    ("7", 7), ("seven", 7),
    ("8", 8), ("eight", 8),
    ("9", 9), ("nine", 9),
]


def extract_digits_part_two(line: str) -> [int]:
    result = []

    rest = line
    found_prefix = False
    while rest:
        for prefix, digit in PREFIXES_TO_DIGITS:
            if rest.startswith(prefix):
                found_prefix = True
                result.append(digit)
                rest = rest.removeprefix(prefix)

        if not found_prefix:
            rest = rest[1:]
        found_prefix = False

    return result


if __name__ == '__main__':
    main()
