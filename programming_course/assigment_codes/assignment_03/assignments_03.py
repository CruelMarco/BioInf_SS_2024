# Task 1

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
    pass


def rearrange_parcels(stacks, moves):
    pass

# Task 2

def pwm(filename):

    with open(filename, "r") as file:
    
        sequences = file.readlines()
    
        n = len(sequences[0].strip()) 

    bases = ["A", "C", "G", "T"]
    
    pwm_matrix = [[0] * n for _ in range(4)] 

    for sequence in sequences:
    
        sequence = sequence.strip().upper()  
    
        for j, base in enumerate(sequence):
    
            pwm_matrix[bases.index(base)][j] += 1  

    return pwm_matrix




    pass

def consensus_sequence(pwm):

    bases = ["A", "C", "G", "T"]
    
    n = len(pwm[0])
    
    consensus_seqs = [""] 

    for j in range(n): 
    
        new_seqs = []
    
        for seq in consensus_seqs:  
    
            max_count = max(pwm[i][j] for i in range(4)) 
    
            for i, base in enumerate(bases):
    
                if pwm[i][j] == max_count:
    
                    new_seqs.append(seq + base)  
    
        consensus_seqs = new_seqs  

        consensus_seqs = sorted(consensus_seqs)

    return consensus_seqs



    pass

# Task 3

def solve(n, operations):

    calc_elemets = operations.split(" ")

    operation_seq = calc_elemets[::2]

    num_seq = calc_elemets[1::2]

    if len(operation_seq) != len(num_seq):

        return -1

    else:

        for i in range (len(operation_seq)):

            match operation_seq[i]:

                case "add":

                    n = n + int(num_seq[i])
                
                case "mul":

                    n = n * int(num_seq[i])

                case "div":

                    n = n / int(num_seq[i])

                case "mod":

                    n = n % int(num_seq[i])

        return n


    pass