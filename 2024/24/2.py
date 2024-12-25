import graphviz


def solve(input_str: str) -> str:
    lines = input_str.strip().split("\n")

    inputs = {}
    gates = {}

    for line in lines:
        parts = line.split(" ")
        match parts:
            case [input_name, value]:
                inputs[input_name.replace(":", "")] = int(value)

            case [a, op, b, _, output]:
                gates[output] = (op, a, b)

            case x:
                if x != [""]:
                    raise ValueError(f"Invalid line: {x}")

    # Evaluate the gates
    def eval_gate(gate):
        op, a, b = gates[gate]
        if op == "AND":
            return eval_input(a) & eval_input(b)
        elif op == "OR":
            return eval_input(a) | eval_input(b)
        elif op == "XOR":
            return eval_input(a) ^ eval_input(b)
        else:
            raise ValueError(f"Invalid operator: {op}")

    def eval_input(input_name):
        if input_name in inputs:
            return inputs[input_name]
        else:
            return eval_gate(input_name)

    results = {}
    for gate in gates:
        results[gate] = eval_gate(gate)

    visualize_graph(gates)

    # Sort the results hash by key
    sorted_results = dict(sorted(results.items()))

    # Concatenate all the z bits
    binary_number = ""

    for key in sorted_results:
        if key[0] == "z":
            binary_number += str(sorted_results[key])

    # Reverse the bits
    binary_number = binary_number[::-1]

    # Convert the binary number to a decimal number
    decimal_number = int(binary_number, 2)

    return str(decimal_number)


def visualize_graph(gates, filename="graph"):
    dot = graphviz.Digraph(comment="Gates Graph")
    for output, (op, a, b) in gates.items():
        dot.node(a, a)
        dot.node(b, b)
        dot.node(output, output)
        dot.edge(a, output, label=op)
        dot.edge(b, output, label=op)
    dot.render(filename, format="png")


def check(input_file, func):
    with open(input_file, "r") as f:
        input_data = f.read()
    return func(input_data)


if __name__ == "__main__":
    print(check("sample-input", solve))
    print(check("real-input", solve))
