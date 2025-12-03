import re


def is_repeated(num: int):
    num_str = str(num)

    if len(num_str) % 2:
        return False

    split = 0
    middle = len(num_str) // 2

    return num_str[:middle] == num_str[middle:]


def evaluate_expression(input_str):
    ranges = input_str.split(",")

    return sum(map(lambda range_str: sum(i if is_repeated(i) else 0 for i in range(int(range_str.split("-")[0]), int(range_str.split("-")[1]) + 1)), input_str.split(",")))



def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def main():
    print(check('sample-input', evaluate_expression))
    print(check('real-input', evaluate_expression))

if __name__ == '__main__':
    main()