
import itertools as it

# Task 1
def anagrams(words):

  anagram_groups = {}

  for word in words:

    sorted_word = "".join(sorted(word))

  
    if sorted_word in anagram_groups:
      
      anagram_groups[sorted_word].add(word)

    else:
      
      anagram_groups[sorted_word] = {word}  

  largest_group = max(anagram_groups.values(), key=len)

  return largest_group
  pass


# Task 2
def hamming_distance(filename):

        f = open(filename, 'r')

        lines = f.readlines()

        lines = [i.strip() for i in lines ]

        valid_chars = set("ACGTU")

        for seq in lines:

            for char in seq.upper():

                if char not in valid_chars:

                    return (-1,-1)
        if not all(len(seq) == len(lines[0]) for seq in lines):

            return (-1, -1)

        line = [i.upper().replace("U" , "T") for i in lines]

        combinations = []

        for i in range(len(line)):

            for j in range(i+1, len(line)):

                combinations.append([line[i] , line[j]])

        def hamming_dist(str1, str2): 
            i = 0
            count = 0

            for i in range(len(str1)):

                if(str1[i] != str2[i]):

                    count = count + 1
                i = i + 1
            
            return count

        distance = []

        for k in combinations:

            str1 , str2 = k[0], k[1]

            if len(str1) != len(str2):

                return(-1,-1)

            else:

                dist = hamming_dist(str1, str2)

                distance.append(dist)

        min_distance = min(distance)

        max_distance = max(distance)

        return (min_distance , max_distance)
        


# Task 3
def common_kmers(fasta, k):

    sequences = []

    current_sequence = ""


    with open(fasta, 'r') as file:

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


    pass


# Task 4
def is_vampire(n):

    num_str = str(n)

    num_itr = it.permutations(num_str, len(num_str))

    for num_list in num_itr:

        num_1 = ''.join(num_list)

        fang_1, fang_2  = num_1[:int(len(num_1)/2)], num_1[int(len(num_1)/2):]

        if fang_1[-1] == '0' and fang_2[-1] == '0':

            continue

        if int(fang_1) * int(fang_2) == n:

            return True
        
    if len(num_str) % 2 == 1:

        return False

    pass

def vampire_generator():

    n = 1260 
    
    while True:

        if is_vampire(n):

            yield n
            
        n += 1 
    pass




    