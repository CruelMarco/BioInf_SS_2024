def common_kmers(fasta_filename, k):

    sequences = []

    current_sequence = ""


    with open(fasta_filename, 'r') as file:

        for line in file:

            if line.startswith('>'):  # Header line

                if current_sequence:

                    sequences.append(current_sequence)

                    current_sequence = ""  # Reset for the next sequence

            else: 

                current_sequence += line.strip()

    
    if current_sequence:

        sequences.append(current_sequence)

    
    if not sequences:

        return set()  

    common_kmers_set = set()

    for i in range(len(sequences[0]) - k + 1):

        kmer = sequences[0][i:i+k]

        if all(kmer in seq for seq in sequences[1:]):  

            common_kmers_set.add(kmer)

    return common_kmers_set

kmers = common_kmers("ass_02.3.fasta", 8)

print(kmers)
