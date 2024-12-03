import re

def evaluate_expression(input_str):
    matches = re.findall(r'mul\((\d+),(\d+)\)', input_str)
    result = sum(int(a) * int(b) for a, b in matches)
    return result

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def main():
    print(check('sample-input', evaluate_expression))
    print(check('real-input', evaluate_expression))

if __name__ == '__main__':
    main()