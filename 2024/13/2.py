import itertools
import re
from collections import deque
import heapq

def heuristic(x, y, prize_x, prize_y):
    return abs(prize_x - x) + abs(prize_y - y)

def find_min_tokens(buttons, prize):
    ax, ay, ac = buttons['A']
    bx, by, bc = buttons['B']
    prizex, prizey = prize

    det = ax*by-bx*ay

    i = round((by*prizex-bx*prizey)/det)
    j = round((-ay*prizex+ax*prizey)/det)

    if ax*i+bx*j == prizex and ay*i+by*j == prizey:
        return i*3+j
    return 0

def solve(input_str):
    lines = input_str.strip().split('\n')
    total_prizes = 0
    total_tokens = 0

    for i in range(0, len(lines), 4):
        button_a = tuple(map(int, re.findall(r'\d+', lines[i]))) + (3,)
        button_b = tuple(map(int, re.findall(r'\d+', lines[i+1]))) + (1,)
        prize = tuple(map(int, re.findall(r'\d+', lines[i+2])))

        prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)

        buttons = {'A': button_a, 'B': button_b}
        total_tokens += find_min_tokens(buttons, prize)

    return total_tokens

def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
    print("Sample Input Result:", solve(input_str))

    with open('real-input', 'r') as file:
        input_str = file.read()
    print("Real Input Result:", solve(input_str))

if __name__ == '__main__':
    main()
