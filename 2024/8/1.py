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

                # Calculate potential antinodes
                an_one = (2 * points[j][0] - points[i][0], 2 * points[j][1] - points[i][1])
                an_two = (2 * points[i][0] - points[j][0], 2 * points[i][1] - points[j][1])

                print(an_one, an_two)

                # Check how many are in bounds
                if an_one[0] >= 0 and an_one[0] < len(problem) and an_one[1] >= 0 and an_one[1] < len(problem[0]):
                    # Check if the antinode is a '.' or an antenna of the same frequency
                    antinodes.add(an_one)

                if an_two[0] >= 0 and an_two[0] < len(problem) and an_two[1] >= 0 and an_two[1] < len(problem[0]):
                    # Check if the antinode is a '.' or an antenna of the same frequency
                    antinodes.add(an_two)

    return len(antinodes)

if __name__ == "__main__":
    main()