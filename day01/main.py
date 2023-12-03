from utils import line_generator, check


def main():
    check(part_one('test_input_part_one.txt'), 142)
    print(part_one('puzzle_input.txt'))

    check(part_two('test_input_part_two.txt'), 281)
    print(part_one('puzzle_input.txt'))


def part_one(filename: str) -> int:
    result = [to_calibration_value(line) for line in line_generator(filename)]
    return sum(result)


def part_two(filename: str) -> int:
    return 0


def to_calibration_value(line: str):
    only_digits = [int(char) for char in line if char.isdigit()]
    return int(f'{only_digits[0]}{only_digits[-1]}')


if __name__ == '__main__':
    main()
