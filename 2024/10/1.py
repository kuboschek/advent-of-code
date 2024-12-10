def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

def main():
    print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def solve(input_str: str):
    grid = load_from_string(input_str)

    # Convert grid to ints
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = int(grid[i][j])

    trailheads = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    
    solution = 0
    for trailhead in trailheads:
        peak_count = count_peaks(grid, trailhead)
        print(f"Trailhead {trailhead} has {peak_count} peaks reachable")
        solution += peak_count


    return solution

# Count the number of peaks reachable from a given position
# A peak is a cell with value 9
# A peak is reachable if there is a path that increments in steps of 1
# and does not decrease in value
def count_peaks(grid, position, visited=None):
    if visited is None:
        visited = set()

    if position in visited:
        return 0

    visited.add(position)

    if grid[position[0]][position[1]] == 9:
        return 1

    height = grid[position[0]][position[1]]
    neighbours = [
        (position[0] - 1, position[1]),  # north
        (position[0] + 1, position[1]),  # south
        (position[0], position[1] + 1),  # east
        (position[0], position[1] - 1)   # west
    ]

    peak_count = 0
    for neighbour in neighbours:
        if (neighbour[0] >= 0 and neighbour[0] < len(grid) and
            neighbour[1] >= 0 and neighbour[1] < len(grid[0]) and
            grid[neighbour[0]][neighbour[1]] - height == 1):
            print(f"Moving from {position} to {neighbour} with height {grid[neighbour[0]][neighbour[1]]}")
            peak_count += count_peaks(grid, neighbour, visited)
    return peak_count

if __name__ == '__main__':
    main()