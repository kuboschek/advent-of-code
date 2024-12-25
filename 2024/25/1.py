import numpy as np


def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split("\n")]


def main():
    print(check("sample-input", solve))
    print(check("real-input", solve))


def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def solve(input_str: str) -> str:
    grids = input_str.split("\n\n")

    grids = [load_from_string(grid) for grid in grids]

    locks = [grid for grid in grids if grid[0][0] == "#"]
    keys = [grid for grid in grids if grid[0][0] == "."]

    return count_fitting_pairs(locks, keys)


def schematic_to_heights(schematic: list[list[str]], is_lock: bool) -> list[int]:
    heights = []
    for col in zip(*schematic):
        if is_lock:
            height = (
                next((i for i, cell in enumerate(col) if cell == "."), len(col)) - 1
            )
        else:
            height = next(
                (i for i, cell in enumerate(reversed(col)) if cell == "."), len(col) - 1
            )
        heights.append(height)
    return heights


def count_fitting_pairs(locks: list[list[str]], keys: list[list[str]]) -> int:
    lock_heights = [schematic_to_heights(lock, is_lock=True) for lock in locks]
    key_heights = [schematic_to_heights(key, is_lock=False) for key in keys]

    fitting_pairs = 0

    for lock in lock_heights:
        for key in key_heights:
            if all(l + k < len(locks[0]) for l, k in zip(lock, key)):
                fitting_pairs += 1

    return fitting_pairs


if __name__ == "__main__":
    main()
