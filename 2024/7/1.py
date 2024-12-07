from itertools import product
from operator import add, mul
from concurrent.futures import ThreadPoolExecutor

def main():
    print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def solve(input_str: str):
    problems = input_str.splitlines()

    def solve_problem(problem):
        target, values = problem.split(":")
        target = int(target.strip())
        values = list(map(int, values.split()))

        operator_tests = product([add, mul], repeat=len(values) - 1)

        for operators in operator_tests:
            result = values[0]
            for i, operator in enumerate(operators):
                result = operator(result, values[i + 1])

            if result == target:
                return target
        return 0

    with ThreadPoolExecutor() as executor:
        results = executor.map(solve_problem, problems)

    return sum(results)

if __name__ == "__main__":
    main()