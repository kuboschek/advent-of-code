import networkx as nx

def solve(input_str: str) -> str:
    lines = input_str.strip().split("\n")
    
    # Build an undirected graph from the input
    G = nx.Graph()
    for line in lines:
        a, b = line.strip().split("-")
        G.add_edge(a, b)
    
    # Find all maximal cliques in the graph
    cliques = nx.find_cliques(G)
    
    # Convert the generator to a list so we can iterate multiple times if needed
    # but here we just find the largest once:
    largest_clique = []
    for c in cliques:
        if len(c) > len(largest_clique):
            largest_clique = c
    
    # Sort the node names and join them with commas for the output
    return ",".join(sorted(largest_clique))

def check(input_file, func):
    with open(input_file, 'r') as f:
        input_data = f.read()
    return func(input_data)

if __name__ == "__main__":
    print(check("sample-input", solve))
    print(check("real-input", solve))
