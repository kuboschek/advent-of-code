def can_construct(design, patterns):
    # Create a set of patterns for quick lookup
    pattern_set = set(patterns)
    
    # Use dynamic programming to check if the design can be constructed
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Base case: empty design can always be constructed
    
    for i in range(1, len(design) + 1):
        for j in range(i):
            if dp[j] and design[j:i] in pattern_set:
                dp[i] = True
                break
    
    return dp[len(design)]

def count_possible_designs(patterns, designs):
    count = 0
    for design in designs:
        if can_construct(design, patterns):
            count += 1
    return count

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
        patterns = lines[0].split(', ')
        designs = lines[2:]  # Skip the blank line
    return patterns, designs

# Read inputs from files
sample_patterns, sample_designs = read_input('sample-input')
real_patterns, real_designs = read_input('real-input')

# Compute results
sample_result = count_possible_designs(sample_patterns, sample_designs)
real_result = count_possible_designs(real_patterns, real_designs)

# Print results
print(f'Sample Result: {sample_result}')
print(f'Real Result: {real_result}')