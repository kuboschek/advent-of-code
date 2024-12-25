from itertools import combinations


def solve(input_str: str) -> int:
    lines = input_str.strip().split("\n")

    # Build adjacency list for undirected graph
    adj = {}
    for line in lines:
        a, b = line.strip().split("-")
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)

    all_nodes = sorted(adj.keys())
    fully_connected_triples = []

    # Check all combinations of three
    for combo in combinations(all_nodes, 3):
        a, b, c = combo
        if b in adj[a] and c in adj[a] and c in adj[b]:
            fully_connected_triples.append(combo)

    # Count how many contain a name starting with 't'
    count_t = sum(
        any(x.startswith("t") for x in group) for group in fully_connected_triples
    )
    return count_t


def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


if __name__ == "__main__":
    print(check("sample-input", solve))
    print(check("real-input", solve))
