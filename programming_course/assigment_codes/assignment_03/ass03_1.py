def read_config(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    stacks = {}
    moves = []

    # Determine the number of stacks by the last line of parcels
    num_stacks = len(lines[-3].split())

    # Initialize stacks
    for i in range(1, num_stacks + 1):
        stacks[i] = []

    # Parse stacks from the file
    for line in lines[:-2]:  # the last two lines are move instructions
        parcels = line.split()
        for i, parcel in enumerate(parcels):
            if parcel != ' ':
                stack_num = i + 1
                stacks[stack_num].append(parcel)

    # Reverse each stack to have the correct order (bottom to top)
    for stack in stacks:
        stacks[stack].reverse()

    # Parse move instructions
    for line in lines[-2:]:
        if line.startswith('move'):
            parts = line.split()
            num_parcels = int(parts[1])
            from_stack = int(parts[3])
            to_stack = int(parts[5])
            moves.append((num_parcels, from_stack, to_stack))

    return stacks, moves

# Example usage:
file_path = 'ass_03.1.txt'
stacks, moves = read_config(file_path)
print(stacks)
print(moves)
