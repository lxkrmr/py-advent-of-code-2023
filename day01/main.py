from utils import check, line_generator


def main():
    check(part_one('test_input_part_one.txt'), 142)
    print(part_one('puzzle_input.txt'))

    check(part_two('test_input_part_two.txt'), 281)
    print(part_two('puzzle_input.txt'))


def part_one(filename: str) -> int:
    return sum([
        to_calibration(extract_digits_part_one(line))
        for line
        in line_generator(filename)
    ])


def part_two(filename: str) -> int:
    return sum([
        to_calibration(extract_digits_part_two(line))
        for line
        in line_generator(filename)
    ])


def extract_digits_part_one(line: str) -> [int]:
    return [int(char) for char in line if char.isdigit()]


def extract_digits_part_two(line: str) -> [int]:
    result = []

    rest = line
    while rest:
        if starts_with_digit(rest):
            digit, rest = extract_digit(rest)
            result.append(digit)
        elif starts_with_digit_as_word(rest):
            digit, rest = extract_digit_as_word(rest)
            result.append(digit)
        else:
            rest = rest[1:]

    return result


def starts_with_digit(rest: str) -> bool:
    return rest[0].isdigit()


def extract_digit(rest):
    return int(rest[0]), rest[1:]


WORDS_TO_DIGIT = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def starts_with_digit_as_word(rest: str) -> bool:
    for word in WORDS_TO_DIGIT:
        if rest.startswith(word):
            return True

    return False


def extract_digit_as_word(rest: str) -> (int, str):
    for word in WORDS_TO_DIGIT:
        if rest.startswith(word):
            return WORDS_TO_DIGIT[word], rest[len(word):]

    return None, rest


def to_calibration(digits: [int]) -> int:
    return int(f'{digits[0]}{digits[-1]}')


if __name__ == '__main__':
    main()
