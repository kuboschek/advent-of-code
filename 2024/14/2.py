import itertools
import re
import tqdm

def parse_input(input_str):
    robots = []
    for line in input_str.strip().split('\n'):
        p, v = line.split(' v=')
        p = tuple(map(int, re.findall(r'-?\d+', p)))
        v = tuple(map(int, re.findall(r'-?\d+', v)))
        robots.append((p, v))
    return robots

def move_robots(robots, width, height, seconds):
    new_positions = []
    for (px, py), (vx, vy) in robots:
        new_px = (px + vx * seconds) % width
        new_py = (py + vy * seconds) % height
        new_positions.append((new_px, new_py))
    return new_positions

def move_one_robot(robot, width, height, seconds):
    (px, py), (vx, vy) = robot
    new_px = (px + vx * seconds) % width
    new_py = (py + vy * seconds) % height
    return (new_px, new_py)
    
def time_to_reach_point(robot, point, width, height):
    (px, py), (vx, vy) = robot
    tx, ty = point

    if vx == 0 and px != tx:
        return float('inf')  # Robot will never reach the target x-coordinate
    if vy == 0 and py != ty:
        return float('inf')  # Robot will never reach the target y-coordinate

    if vx != 0:
        time_x = (tx - px) / vx
        if time_x < 0 or (tx - px) % vx != 0:
            time_x = float('inf')
    else:
        time_x = 0

    if vy != 0:
        time_y = (ty - py) / vy
        if time_y < 0 or (ty - py) % vy != 0:
            time_y = float('inf')
    else:
        time_y = 0

    if time_x == float('inf') and time_y == float('inf'):
        return float('inf')

    if time_x == float('inf'):
        return time_y
    if time_y == float('inf'):
        return time_x

    if time_x == time_y:
        return time_x

    return float('inf')

def count_robots_in_quadrants(positions, width, height):
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0, 0, 0, 0]

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1

    return quadrants

def check_christmas_tree(positions, width, height):
    tree_pattern = [
        "....*....",
        "...***...",
        "..*****..",
        ".*******.",
        "*********",
        "....*....",
        "....*...."
    ]
    tree_height = len(tree_pattern)
    tree_width = len(tree_pattern[0])
    
    for y in range(height - tree_height + 1):
        for x in range(width - tree_width + 1):
            match = True
            for dy in range(tree_height):
                for dx in range(tree_width):
                    if tree_pattern[dy][dx] == '*' and (x + dx, y + dy) not in positions:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

def solve(input_str):
    robots = parse_input(input_str)
    width, height = 101, 103

    for seconds in tqdm.tqdm(range(1, 100000)):  # Check up to 1000 seconds
        positions = move_robots(robots, width, height, seconds)
        if check_christmas_tree(set(positions), width, height):
            print(f"Christmas tree detected after {seconds} seconds!")
            return seconds

    return -1  # Return -1 if no Christmas tree is detected within 1000 seconds

def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
    print("Sample Input Result:", solve(input_str))

    with open('real-input', 'r') as file:
        input_str = file.read()
    print("Real Input Result:", solve(input_str))

if __name__ == '__main__':
    main()
