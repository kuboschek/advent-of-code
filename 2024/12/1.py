def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < max_x - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < max_y - 1:
        neighbors.append((x, y + 1))
    return neighbors

def calculate_area_and_perimeter(grid, x, y, visited):
    stack = [(x, y)]
    plant_type = grid[x][y]
    area = 0
    perimeter = 0
    max_x = len(grid)
    max_y = len(grid[0])
    
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        local_perimeter = 4
        
        for nx, ny in get_neighbors(cx, cy, max_x, max_y):
            if grid[nx][ny] == plant_type:
                stack.append((nx, ny))
                local_perimeter -= 1
        
        perimeter += local_perimeter
    
    return area, perimeter

def solve(input_str):
    grid = load_from_string(input_str)
    visited = set()
    total_price = 0
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                area, perimeter = calculate_area_and_perimeter(grid, x, y, visited)
                total_price += area * perimeter
    
    return total_price

def main():
    print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

if __name__ == '__main__':
    main()