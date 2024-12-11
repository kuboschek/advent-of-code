from functools import reduce

def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

def main():
    #print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def iterate(stones):
    def reducer(new_stones, stone):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
        return new_stones

    return reduce(reducer, stones, [])

def solve(input_str: str):
    stones = list(map(int, input_str.split(' ')))

    for i in range(25):
        print(i)
        stones = iterate(stones)

    return len(stones)


if __name__ == '__main__':
    main()