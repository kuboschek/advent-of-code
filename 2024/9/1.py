def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

def main():
    print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def expand_layout(input: str) -> list[str]:
    disk_layout = []
    file_id = 0

    for index, char in enumerate(input):
        int_char = int(char)
        if index % 2 == 0:
            disk_layout.extend([str(file_id)] * int_char)
            file_id += 1
        else:
            disk_layout.extend(["."] * int_char)

    return disk_layout

def defragment_disk(disk_map: list[str]) -> list[str]:
    # Move a block from end of disk to left-most empty space
    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            for j in range(len(disk_map) - 1, i, -1):
                if disk_map[j] != ".":
                    disk_map[i] = disk_map[j]
                    disk_map[j] = "."
                    break
    
    return disk_map

def calculate_checksum(disk_map: str) -> int:
    checksum = 0
    for pos, block in enumerate(disk_map):
        if block != ".":
            checksum += pos * int(block)
    return checksum

def solve(input_str: str):
    full_layout = expand_layout(input_str)
    print(full_layout)

    disk_map = defragment_disk(full_layout)
    print(disk_map)

    checksum = calculate_checksum(disk_map)
    return checksum

if __name__ == "__main__":
    main()