import re
import numpy as np


def main():
    print(check('sample-input', count_xmas))
    print(check('real-input', count_xmas))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def count_xmas(input_str: str):
    lines = input_str.strip().split('\n')
    matrix = np.array([list(line) for line in lines])
    count = 0

    def is_xmas_pattern(matrix, i, j):
        return all(matrix[i + di][j + dj] == 'M' for di, dj in [(0, 0), (0, 2)]) and \
               all(matrix[i + di][j + dj] == 'A' for di, dj in [(1, 1)]) and \
               all(matrix[i + di][j + dj] == 'S' for di, dj in [(2, 0), (2, 2)])


    def count_patterns(matrix):
        local_count = 0
        for i in range(matrix.shape[0] - 2):
            for j in range(matrix.shape[1] - 2):
                submatrix = matrix[i:i+3, j:j+3]
                if is_xmas_pattern(matrix, i, j):
                    local_count += 1
        return local_count

    count += count_patterns(matrix)
    print(f"Count plain {count}")
    count += count_patterns(np.flipud(matrix))
    print(f"Count upside down {count}")
    count += count_patterns(np.flipud(matrix.T))
    print(f"Count upside-down transposed {count}")
    count += count_patterns(matrix.T)
    print(f"Count transpose {count}")

    return count


if __name__ == "__main__":
    main()