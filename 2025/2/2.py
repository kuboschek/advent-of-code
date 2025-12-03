import re


def is_repeated(num: int) -> bool:
    num_str = str(num)

    if len(num_str) == 1:
        return False # No repeats possible on length one.

    for split in range(1, len(num_str) // 2 + 1):
        parts = [(num_str[i:i+split]) for i in range(0, len(num_str), split)]

        if len(set(parts)) == 1:
            return True

    return False



def evaluate_expression(input_str):
    ranges = input_str.split(",")

    return sum(map(lambda range_str: sum(i if is_repeated(i) else 0 for i in range(int(range_str.split("-")[0]), int(range_str.split("-")[1]) + 1)), input_str.split(",")))



def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def main():
    print(is_repeated(1010))
    print(is_repeated(111))
    print(is_repeated(123123123))
    print(check('sample-input', evaluate_expression))
    print(check('real-input', evaluate_expression))

if __name__ == '__main__':
    main()