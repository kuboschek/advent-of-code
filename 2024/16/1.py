from collections import deque
import heapq

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
    maze = load_from_string(input_str)
    start, end = None, None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    # Find start and end positions
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)

    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

    # Priority queue to find the cheapest path
    pq = [(0, start[0], start[1], 0)]  # (cost, x, y, direction)
    visited = set()

    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        if (x, y) == end:
            return cost

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_cost = cost + 1
                if direction != -1 and direction != i:
                    new_cost += 1000  # Turning cost
                heapq.heappush(pq, (new_cost, new_x, new_y, i))

    return -1  # If no path is found

if __name__ == "__main__":
    main()

