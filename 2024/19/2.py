def count_ways_to_construct(design, patterns):
    # Create a set of patterns for quick lookup
    pattern_set = set(patterns)
    
    # Use dynamic programming to count the number of ways to construct the design
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # Base case: there's one way to construct an empty design
    
    for i in range(1, len(design) + 1):
        for j in range(i):
            if design[j:i] in pattern_set:
                dp[i] += dp[j]
    
    return dp[len(design)]

def total_ways_to_construct(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_construct(design, patterns)
    return total_ways

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
sample_result = total_ways_to_construct(sample_patterns, sample_designs)
real_result = total_ways_to_construct(real_patterns, real_designs)

# Print results
print(f'Sample Result: {sample_result}')
print(f'Real Result: {real_result}')