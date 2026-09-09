# Conditional probability includes context into the sequence unlike frequency probability that is entirely dependent on counts.

# The idea is that there will be nested dictionaries; a dictionary whose values are another dictionary

sequence = [0,1,2,1,3]

transitions = {}

for i in range(len(sequence) - 1):
    current = sequence[i]
    next_item = sequence[i + 1]

    if current not in transitions:
        transitions[current] = {}
    # the block of code aboce creates the dictionaries
    
    print(current, "->", next_item)

    