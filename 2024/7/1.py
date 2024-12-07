from itertools import combinations, combinations_with_replacement, permutations
from operator import add, mul

def main():
    print(check('/home/leo/dev/advent-of-code/2024/7/sample-input', solve))
    print(check('/home/leo/dev/advent-of-code/2024/7/real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def solve(input_str: str):
    problems = input_str.splitlines()

    output = 0

    operator_test_map = {}

    for problem in problems:
        target, values = problem.split(":")

        target = int(target.strip())
        values = list(map(int, values.split()))

        # Generate all possible operator combinations with replacement of length len(values) - 
        # For input of length 3, this would generate all possible combinations of add and mul operators


        # Build operator_tests
        operator_tests = []
        for operators in combinations_with_replacement([add, mul], len(values) - 1):
            for operator_order in permutations(operators):
                operator_tests.append(operator_order)

        # Filter out duplicate operator tests
        operator_tests = list(set(operator_tests))

        for operators in operator_tests:
            # Format the equation nicely
            # equation = ""
            # for i, value in enumerate(values):
            #     equation += str(value)
            #     if i < len(operators):
            #         equation += " " + operators[i].__name__ + " "

            # print(equation)

            # Apply the operators in between the values
            result = values[0]
            for i, operator in enumerate(operators):
                result = operator(result, values[i + 1])

            if result == target:
                output += target
                break

    return output

if __name__ == "__main__":
    main()