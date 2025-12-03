import itertools

def evaluate_expression(input_str: str):
    strings = input_str.splitlines()

    return sum(map(lambda string: max(map(lambda combo: int("".join(combo)), itertools.combinations(string, 2))), strings))


def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def main():
    print(check('sample-input', evaluate_expression))
    print(check('real-input', evaluate_expression))

if __name__ == '__main__':
    main()