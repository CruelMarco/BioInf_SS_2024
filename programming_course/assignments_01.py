def process_list(mylist):

  for i in range(len(mylist)):

    for j in range(len(mylist)):
        if mylist[j] % 2 == 0: 

            mylist[j] //= 2   #if even divide by two
        else:

            mylist[j] *= 2 #if odd multiply by two
               
        if (j) % 7 == 0:      #to check if k is a multiple of 7
            mylist[j] += j      #to add the position value

    max_value = max(mylist)

    return max_value
    pass

def DNA_complement(seq):

    changed_dna = ""

    for i in seq[::-1]:

        if i == "A":

            changed_dna = changed_dna + "T"

        elif i == "T":

            changed_dna = changed_dna + "A"

        elif i == "G":

           changed_dna = changed_dna + "C"

        else:

            changed_dna = changed_dna + "G"

    return(changed_dna)
    pass

def list_kmers(s, k): # s - DNA Sequence k - integer

    if k > len(s):

        return []
    
    else:

        kmers = [s[i:i+k] for i in range(len(s)-k+1)]

    return kmers
    pass
    
def number_of_unique(s, k):

    kmers = list_kmers(s, k)
    kmer_count = {}
    for kmer in kmers:
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1
    unique_kmers = sum(1 for count in kmer_count.values() if count == 1)
    return unique_kmers
    pass

def kmer_code(kmer):

    code = 0

    for i in range(len(kmer)):

        if kmer[i] == 'A':
            
            code = code << 2
        
        elif kmer[i] == 'C':
            
            code = (code << 2) + 1
        
        elif kmer[i] == 'G':
            
            code = (code << 2) + 2
        
        elif kmer[i] == 'T':
            
            code = (code << 2) + 3
    
    return code
    pass

def kmer_decode(code, k):

    kmer = ''
    
    for i in range(k):
        
        if code & 3 == 0:
        
            kmer = 'A' + kmer
        
        elif code & 3 == 1:
        
            kmer = 'C' + kmer
        
        elif code & 3 == 2:
        
            kmer = 'G' + kmer
        
        elif code & 3 == 3:
        
            kmer = 'T' + kmer
        
        code = code >> 2
    
    return kmer

    pass



