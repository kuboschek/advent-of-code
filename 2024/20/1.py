from collections import deque

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = [list(line) for line in file.read().strip().split('\n')]
    return lines

def find_start_end(grid):
    start, end = None, None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return start, end

def bfs(grid, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    
    return float('inf')  # If no path found

def find_cheats(grid, start, end, shortest_path_length):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cheats = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                grid[i][j] = '.'
                new_path_length = bfs(grid, start, end)
                grid[i][j] = '#'
                time_saved = shortest_path_length - new_path_length
                if time_saved >= 100:
                    cheats.append((time_saved, (i, j)))
    
    return cheats

def main():
    grid = parse_input('real-input')
    start, end = find_start_end(grid)
    shortest_path_length = bfs(grid, start, end)
    cheats = find_cheats(grid, start, end, shortest_path_length)
    
    print(f'Number of cheats that save at least 100 picoseconds: {len(cheats)}')

if __name__ == '__main__':
    main()