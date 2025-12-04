import itertools

def evaluate_expression(input_str: str):
    sum = 0
    
    for line in input_str.splitlines():
        sum += int(get_joltage(line))

    return sum

def get_joltage(string, length=12, current=""):
    if length > len(string):
        return None
    if length==0:
        return current
    if length==1:
        return current + max(string)

    for c in "987654321":
        if c in string:
            index = string.index(c)
            substr = string[index+1:]
            if (result := get_joltage(substr, length-1, current+c)) is not None:
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