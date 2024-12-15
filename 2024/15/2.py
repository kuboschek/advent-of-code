def load_warehouse(input_str):
    data = input_str.strip('\n').split('\n')
    box, moves = '\n'.join(data).split('\n\n')
    warehouse = []
    robot_start = None
    expand_map = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    }

    for i, line in enumerate(box.split('\n')):
        row = []
        for j, char in enumerate(line):
            if char == '@':
                robot_start = (i, 2 * j)
            for expanded_char in expand_map[char]:
                row.append(expanded_char)
        warehouse.append(row)

    return warehouse, robot_start, moves.replace('\n', '')

def find_robot(warehouse):
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == '@':
                return x, y
    return None

def move_robot(warehouse, robot_position, moves):
    direction_map = {
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
    }

    for move in moves:
        robot_x, robot_y = robot_position
        dx, dy = direction_map[move]
        new_x, new_y = (robot_x + dx, robot_y + dy)

        if warehouse[new_x][new_y] == '.':
            warehouse[robot_x][robot_y] = '.'
            warehouse[new_x][new_y] = '@'
            robot_position = (new_x, new_y)
            continue
        elif warehouse[new_x][new_y] == '#':
            continue

        if dx == 0:
            temp_x, temp_y = new_x, new_y
            distance = 0
            while warehouse[temp_x][temp_y] in {'[', ']'}:
                distance += 1
                temp_x, temp_y = (temp_x + dx, temp_y + dy)

            if warehouse[temp_x][temp_y] == '#':
                continue

            for i in range(distance):
                warehouse[temp_x][temp_y] = warehouse[temp_x - dx][temp_y - dy]
                temp_x, temp_y = (temp_x - dx, temp_y - dy)

            warehouse[new_x][new_y] = '@'
            warehouse[robot_x][robot_y] = '.'
            robot_position = (new_x, new_y)
            continue

        to_push = [{(robot_x, robot_y)}]

        no_wall = True
        all_empty = False
        while no_wall and not all_empty:
            next_push = set()
            all_empty = True
            for current_x, current_y in to_push[-1]:
                if warehouse[current_x][current_y] == '.':
                    continue
                temp_x, temp_y = (current_x + dx, current_y + dy)
                if warehouse[temp_x][temp_y] != '.':
                    all_empty = False

                next_push.add((temp_x, temp_y))

                if warehouse[temp_x][temp_y] == '#':
                    no_wall = False
                    break
                elif warehouse[temp_x][temp_y] == '[':
                    next_push.add((temp_x, temp_y + 1))
                elif warehouse[temp_x][temp_y] == ']':
                    next_push.add((temp_x, temp_y - 1))

            to_push.append(next_push)

        if not no_wall:
            continue

        for i in range(len(to_push) - 1, 0, -1):
            for current_x, current_y in to_push[i]:
                from_x, from_y = (current_x - dx, current_y - dy)
                if (from_x, from_y) in to_push[i - 1]:
                    warehouse[current_x][current_y] = warehouse[from_x][from_y]
                else:
                    warehouse[current_x][current_y] = '.'

        warehouse[robot_x][robot_y] = '.'
        robot_position = (new_x, new_y)

    return warehouse

def show_warehouse(warehouse):
    for row in warehouse:
        print(''.join(row))
    print()

def sum_box_locations(warehouse):
    total = 0
    for i, line in enumerate(warehouse):
        for j, char in enumerate(line):
            if char != '[':
                continue
            total += 100 * i + j
    return total

def solve(input_str):
    warehouse, robot_start, moves = load_warehouse(input_str)
    warehouse = move_robot(warehouse, robot_start, moves)
    show_warehouse(warehouse)
    return sum_box_locations(warehouse)

def main():
    with open("real-input", 'r') as f:
        input_str = f.read()
    print("Sum of box locations:", solve(input_str))

if __name__ == '__main__':
    main()