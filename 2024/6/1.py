import numpy as np


def main():
    print(check('sample-input', count_path))
    print(check('real-input', count_path))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def count_path(input_str: str):
    # Load the input into a numpy grid
    grid = np.array([[i for i in line] for line in input_str.strip().split('\n')])

    # Get starting position of guard ("^")
    start = np.argwhere(grid == '^')[0]


    direction = 0

    try:
        while True:
            # Mark the current position as visited
            grid[tuple(start)] = 'X'

            # If the next position is an obstacle, turn right
            if grid[tuple(start + directions[direction])] == '#':
                direction = (direction + 1) % 4

            # Move in the current direction
            start += directions[direction]


    except IndexError:
        # Count the number of X in the grid
        return np.sum(grid == 'X')

directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

if __name__ == "__main__":
    main()