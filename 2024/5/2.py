from functools import cmp_to_key


def main():
    print(check('sample-input', check_ordering))
    print(check('real-input', check_ordering))

def check(input_file, func):
    with open(input_file) as f:
        input_str = f.read()
    return func(input_str)


def lookup_ordering(a, b, rules_dict):
    # If a and b in rules_dict, return -1
    if a in rules_dict and b in rules_dict[a]:
        return -1
    
    # If b in rules_dict and value is a, return 1
    if b in rules_dict and a in rules_dict[b]:
        return 1
    
    return 0

def check_ordering(input_str: str):
    # Split into rules and orders by blank line
    rules, orders = input_str.strip().split('\n\n')

    # Parse rules into a dictionary
    rules_dict = {}
    for rule in rules.split('\n'):
        key, value = rule.split('|')
        if key not in rules_dict:
            rules_dict[key] = []
        rules_dict[key].append(value)

    # Parse orders into a list
    orders = orders.split('\n')

    # Parse each order into a list
    orders = [order.split(",") for order in orders]

    sum = 0

    # Check each order
    for order in orders:
        check = True

        for i in range(len(order) - 1):
            a, b = order[i], order[i + 1]
            if lookup_ordering(a, b, rules_dict) == 1:
                check = False
                
        if not check:
            sorted_order = sorted(order, key=cmp_to_key(lambda a, b: lookup_ordering(a, b, rules_dict)))
            # Get middle number
            middle = sorted_order[len(sorted_order) // 2]
            sum += int(middle)

    return sum

if __name__ == "__main__":
    main()