import itertools
import re

def find_min_tokens(buttons, prize):
    print(buttons)
    A_x, A_y, A_cost = buttons['A']
    B_x, B_y, B_cost = buttons['B']
    prize_x, prize_y = prize

    min_tokens = float('inf')
    best_combination = None

    for a_presses in range(101):
        for b_presses in range(101):
            if a_presses * A_x + b_presses * B_x == prize_x and a_presses * A_y + b_presses * B_y == prize_y:
                tokens = a_presses * A_cost + b_presses * B_cost
                if tokens < min_tokens:
                    min_tokens = tokens
                    best_combination = (a_presses, b_presses)

    return min_tokens, best_combination

def solve(input_str):
    lines = input_str.strip().split('\n')
    total_prizes = 0
    total_tokens = 0

    for i in range(0, len(lines), 4):
        button_a = tuple(map(int, re.findall(r'\d+', lines[i]))) + (3,)
        button_b = tuple(map(int, re.findall(r'\d+', lines[i+1]))) + (1,)
        prize = tuple(map(int, re.findall(r'\d+', lines[i+2])))

        

        buttons = {'A': button_a, 'B': button_b}
        min_tokens, best_combination = find_min_tokens(buttons, prize)

        if best_combination:
            total_prizes += 1
            total_tokens += min_tokens

    return total_prizes, total_tokens

def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
    print("Sample Input Result:", solve(input_str))

    with open('real-input', 'r') as file:
        input_str = file.read()
    print("Real Input Result:", solve(input_str))

if __name__ == '__main__':
    main()
