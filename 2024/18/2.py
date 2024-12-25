from collections import deque

def load_from_string(s: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(','))) for line in s.strip().split('\n')]

def simulate_falling_bytes(grid_size: int, bytes_positions: list[tuple[int, int]], num_bytes: int) -> list[list[str]]:
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in bytes_positions[:num_bytes]:
        grid[y][x] = '#'
    return grid

def find_shortest_path(grid: list[list[str]]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # down, right, up, left
    start = (0, 0)
    end = (len(grid) - 1, len(grid) - 1)
    queue = deque([(start, 0)])  # (position, steps)
    visited = set([start])

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[ny][nx] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1  # If no path is found

def find_first_blocking_byte(grid_size: int, bytes_positions: list[tuple[int, int]]) -> tuple[int, int]:
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for i, (x, y) in enumerate(bytes_positions):
        grid[y][x] = '#'
        if find_shortest_path(grid) == -1:
            return (x, y)
    return (-1, -1)  # If no blocking byte is found

def solve(input_str: str) -> tuple[int, int]:
    bytes_positions = load_from_string(input_str)
    grid_size = 71

    return find_first_blocking_byte(grid_size, bytes_positions)

def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
    print("Sample Input Result:", solve(input_str))

    with open('real-input', 'r') as file:
        input_str = file.read()
    print("Real Input Result:", solve(input_str))

if __name__ == '__main__':
    main()
