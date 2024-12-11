from functools import reduce
from collections import Counter

def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

def main():
    #print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def iterate(stones_counter):
    new_stones_counter = Counter()

    for stone, count in stones_counter.items():

        if stone == 0:
            new_stones_counter[1] += count

        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            middle = len(stone_str) // 2

            left = int(stone_str[:middle])
            right = int(stone_str[middle:])

            new_stones_counter[left] += count
            new_stones_counter[right] += count
        else:
            new_stones_counter[stone * 2024] += count

    return new_stones_counter

def solve(input_str: str):
    stones = Counter(map(int, input_str.split(' ')))

    for i in range(75):
        print(i)
        stones = iterate(stones)

    return sum(stones.values())


if __name__ == '__main__':
    main()