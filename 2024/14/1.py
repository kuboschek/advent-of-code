import itertools
import re

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

def solve(input_str):
    robots = parse_input(input_str)
    width, height = 101, 103
    seconds = 100

    positions = move_robots(robots, width, height, seconds)
    quadrants = count_robots_in_quadrants(positions, width, height)

    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return safety_factor

def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
    print("Sample Input Result:", solve(input_str))

    with open('real-input', 'r') as file:
        input_str = file.read()
    print("Real Input Result:", solve(input_str))

if __name__ == '__main__':
    main()
