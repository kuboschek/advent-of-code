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
    file_blocks = {}
    current_file = None
    current_span = []

    # Collect file blocks and their positions
    for i, block in enumerate(disk_map):
        if block != ".":
            if block != current_file:
                if current_file is not None:
                    file_blocks[current_file] = current_span
                current_file = block
                current_span = []
            current_span.append(i)
    if current_file is not None:
        file_blocks[current_file] = current_span

    # Move files in order of decreasing file ID number
    for file_id in sorted(file_blocks.keys(), key=int, reverse=True):
        span = file_blocks[file_id]
        file_length = len(span)
        for i in range(len(disk_map) - file_length + 1):
            if all(disk_map[j] == "." for j in range(i, i + file_length)):
                if i < span[0]:  # Ensure only moving closer to the start
                    for j in range(file_length):
                        disk_map[span[j]] = "."
                        disk_map[i + j] = file_id
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
    print(''.join(full_layout))

    disk_map = defragment_disk(full_layout)
    print(''.join(disk_map))

    checksum = calculate_checksum(disk_map)
    return checksum

if __name__ == "__main__":
    main()