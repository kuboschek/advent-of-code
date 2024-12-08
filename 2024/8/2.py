def load_from_string(s: str) -> list[list[str]]:
    return [list(line) for line in s.strip().split('\n')]

def main():
    print(check('sample-input', solve))
    print(check('real-input', solve))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)

def solve(input_str: str):
    problem = load_from_string(input_str)

    locations = {}
    antinodes = set()

    # Get lists of points of all distinct characters
    for i, row in enumerate(problem):
        for j, cell in enumerate(row):
            if cell != '.':
                print(cell, i, j)
                if cell not in locations:
                    locations[cell] = []

                locations[cell].append((i, j))

    for freq, points in locations.items():
        print(freq, points)

        # Iterate through all pairs of points
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                print("Inner")
                print(points[i], points[j])

                # Step forward from the first point to the second point and beyond
                x = points[i][0]
                y = points[i][1]

                print("Step Forward")
                while 0 <= x <= len(problem) and 0 <= y <= len(problem[0]):
                    print(x, y)

                    antinodes.add((x, y))

                    x += points[j][0] - points[i][0]
                    y += points[j][1] - points[i][1]

                # Step backward from the second to the first point and beyond
                x = points[j][0]
                y = points[j][1]

                print("Step Backward")
                while 0 <= x <= len(problem) and 0 <= y <= len(problem[0]):
                    print(x, y)

                    antinodes.add((x, y))

                    x += points[i][0] - points[j][0]
                    y += points[i][1] - points[j][1]



        # Add all antenna positions as antinodes if they are in line with at least two antennas
        if len(points) > 1:
            for point in points:
                antinodes.add(point)

    # Draw all the antinodes on the grid
    for i, row in enumerate(problem):
        for j, cell in enumerate(row):
            if (i, j) in antinodes and cell == '.':
                problem[i][j] = '#'

    # Count characters that are not '.'
    count = 0
    for i, row in enumerate(problem):
        for j, cell in enumerate(row):
            if cell != '.':
                count += 1

    return count

if __name__ == "__main__":
    main()