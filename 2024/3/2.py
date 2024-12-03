import re

def evaluate_expression(input_str):
    matches = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', input_str)
    enabled = True
    result = 0

    for match in matches:
        if match[0] == 'do()':
            enabled = True
        elif match[0] == "don't()":
            enabled = False
        elif match[1] and match[2] and enabled:
            result += int(match[1]) * int(match[2])

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