import numpy as np

def main():
    print(check('sample-input', count_obstruction_positions))
    print(check('real-input', count_obstruction_positions))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def count_obstruction_positions(input_str: str):
    # Load the input into a numpy grid
    grid = np.array([[i for i in line] for line in input_str.strip().split('\n')])

    # Get starting position
    start = np.argwhere(grid == '^')[0]

    possible_positions = []

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == '.' and (i, j) != tuple(start):
                temp_grid = grid.copy()
                temp_grid[i, j] = '#'

                if calc(temp_grid, tuple(start)):
                    possible_positions.append((i, j))

    return len(possible_positions)

def calc(grid, startpos):
    r, c = startpos
    dr, dc = -1, 0
    seen = set()

    while True:
        # Out of bounds?
        if not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]):
            break

        # Hit a wall?
        if grid[r, c] == '#':
            r -= dr
            c -= dc
            dr, dc = dc, -dr
            continue

        k = (r, c, dr, dc)
        if k in seen:
            return True

        seen.add(k)
        r += dr
        c += dc

    return False

if __name__ == "__main__":
    main()