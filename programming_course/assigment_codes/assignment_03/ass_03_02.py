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


def consensus_sequence(pwm):


    bases = ["A", "C", "G", "T"]
    n = len(pwm[0])
    consensus_seqs = [""]  # Start with an empty sequence

    for j in range(n):  # Iterate over positions in the sequence
        new_seqs = []
        for seq in consensus_seqs:  # For each existing sequence
            max_count = max(pwm[i][j] for i in range(4))  # Find max count at position j
            for i, base in enumerate(bases):
                if pwm[i][j] == max_count:
                    new_seqs.append(seq + base)  # Add base if it matches max count
        consensus_seqs = new_seqs  # Replace with the extended sequences

    return sorted(consensus_seqs)  # Sort lexicographically

pwm_matrix = pwm("ass_03.2.txt")  # Replace with your filename
print(pwm_matrix) 


# Example Usage (Using the previously calculated `pwm_matrix`):
consensus_list = consensus_sequence(pwm_matrix)
print(consensus_list) 
