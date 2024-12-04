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
    word = "XMAS"
    count = 0

    def count_overlapping(text, word):
        return sum(1 for i in range(len(text) - len(word) + 1) if text[i:i+len(word)] == word)

    print("rows")

    # Check rows and reverse rows
    for row in matrix:
        print(row)
        count += count_overlapping(''.join(row), word)
        count += count_overlapping(''.join(row[::-1]), word)
        print(count)

    print("cols")

    # Check columns and reverse columns
    for col in matrix.T:
        print(col)
        count += count_overlapping(''.join(col), word)
        count += count_overlapping(''.join(col[::-1]), word)
        print(count)

    print("diags")

    # Check diagonals
    diags = [matrix.diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    diags += [np.fliplr(matrix).diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    for diag in diags:
        print(diag)
        count += count_overlapping(''.join(diag), word)
        count += count_overlapping(''.join(diag[::-1]), word)

        print(count)

    return count


if __name__ == "__main__":
    main()