from utils import line_generator, check


def main():
    check(solve_puzzle_one('test_input.txt'), 142)
    print(solve_puzzle_one('puzzle_input.txt'))


def solve_puzzle_one(filename: str) -> int:
    result = [to_calibration_value(line) for line in line_generator(filename)]
    return sum(result)


def to_calibration_value(line: str):
    only_digits = [int(char) for char in line if char.isdigit()]
    return int(f'{only_digits[0]}{only_digits[-1]}')


if __name__ == '__main__':
    main()
