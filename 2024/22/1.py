def main():
    print(check("sample-input", solve))
    print(check("real-input", solve))


def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


MOD_VALUE = 0b1_00000000_00000000_00000000
BITMASK = 0b11111111_11111111_11111111  # Derived from the MOD_VALUE


# Generates numbers between 0 and 2^24 - 1
def step_prng(seed: int) -> int:
    # Zero out the lowest 8 bits, flip the others
    seed = ((seed << 6) ^ seed) & BITMASK

    # Shift right by 5 bits, XOR with the original seed
    seed = ((seed >> 5) ^ seed) & BITMASK

    # Shift left by 11 bits, XOR with the original seed
    seed = ((seed << 11) ^ seed) & BITMASK
    return seed


def loop_prng(seed: int, n: int) -> int:
    for _ in range(n):
        seed = step_prng(seed)

    return seed


def solve(input_str: str) -> int:
    numbers = list(map(int, input_str.strip().split("\n")))

    output = map(lambda x: loop_prng(seed=x, n=2_000), numbers)

    return sum(output)


if __name__ == "__main__":
    main()
