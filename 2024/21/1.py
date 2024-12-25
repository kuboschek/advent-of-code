# Define the numeric keypad layout

numeric_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [" ", "0", "A"]]


# Define the directional keypad layout

directional_keypad = [[" ", "^", "A"], ["<", "v", ">"]]


# Define the movements for the directional keypad

movements = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


from collections import deque


def bfs(start, target, keypad, movements):
    rows, cols = len(keypad), len(keypad[0])
    queue = deque([(start, "")])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if keypad[x][y] == target:
            return path

        for move, (dx, dy) in movements.items():
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and keypad[nx][ny] != " "
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + move))

    return None


def find_shortest_sequence(code, numeric_keypad, directional_keypad, movements):
    first_sequence = ""
    current_position = (3, 2)  # Starting at 'A' on the numeric keypad

    # Resolving shortest sequence for first keypad

    for char in code:
        path = bfs(current_position, char, numeric_keypad, movements)

        if path is None:
            return None
        first_sequence += path + "A"

        # Print the keypad with the path
        temp_keypad = [row[:] for row in numeric_keypad]
        x, y = current_position
        for move in path:
            dx, dy = movements[move]
            x, y = x + dx, y + dy
            temp_keypad[x][y] = "*"
        for row in temp_keypad:
            print(" ".join(row))
        print()

        for move in path:
            dx, dy = movements[move]
            current_position = (current_position[0] + dx, current_position[1] + dy)

    print("First ", first_sequence)

    final_sequence = first_sequence

    for i in range(2):
        new_sequence = ""
        current_position = (0, 2)  # Starting at 'A' on the directional keypad

        for char in final_sequence:
            path = bfs(current_position, char, directional_keypad, movements)

            if path is None:
                return None

            new_sequence += path + "A"

            temp_keypad = [row[:] for row in directional_keypad]
            x, y = current_position
            for move in path:
                dx, dy = movements[move]
                x, y = x + dx, y + dy
                temp_keypad[x][y] = "*"
            for row in temp_keypad:
                print(" ".join(row))
            print(path)
            print()

            for move in path:
                dx, dy = movements[move]
                current_position = (current_position[0] + dx, current_position[1] + dy)

        final_sequence = new_sequence
        print(f"{i}, {final_sequence}")

    return new_sequence


def calculate_complexity(sequence, code):
    numeric_part = int(code[:-1])  # Ignore the last character 'A'
    return len(sequence) * numeric_part


def main():
    codes = ["029A"]

    total_complexity = 0

    for code in codes:
        sequence = find_shortest_sequence(
            code, numeric_keypad, directional_keypad, movements
        )

        if sequence is not None:
            complexity = calculate_complexity(sequence, code)
            print(
                f"Code: {code}, Length of Sequence: {len(sequence)}, Complexity: {complexity}"
            )
            total_complexity += complexity

    print(f"Total Complexity: {total_complexity}")


if __name__ == "__main__":
    main()
