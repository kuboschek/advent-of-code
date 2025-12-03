import itertools

def evaluate_expression(input_str: str):
    rotations = input_str.splitlines()

    zeros = 0
    position = 50

    for rotation in rotations:
        direction, amount = -1 if rotation[0] == "L" else 1, int(rotation[1:])


        for _ in range(amount):
            position += direction
            position %= 100

            if position == 0:
                zeros += 1

    return zeros


def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def main():
    print(check('sample-input', evaluate_expression))
    print(check('real-input', evaluate_expression))

if __name__ == '__main__':
    main()