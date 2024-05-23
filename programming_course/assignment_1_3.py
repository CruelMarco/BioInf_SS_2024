######1 Write a function list_kmers that, given a DNA sequence s and an integer k,
######returns a list of all k-mers (strings of length k, from left to right, overlapping).
######Handle edge cases correctly (k > |s| ?!).
######2 Write a function number_of_unique_kmers that, given s and k,
######returns the number of unique k-mers in s (k-mers that appear only once).

def list_kmers(s, k): # s - DNA Sequence k - integer

    if k > len(s):

        return []
    
    else:

        kmers = [s[i:i+k] for i in range(len(s)-k+1)]

    return kmers
    
def number_of_unique_kmers(s, k):

    import numpy as np

    kmers = list_kmers(s, k)

    unique_kmers_array = np.unique(kmers)

    return len(unique_kmers_array)

kmer = list_kmers("ACGATCGATC", 5)

print(kmer)

unique_kmer_nos = number_of_unique_kmers("ACGATCGATC", 5)    

print(unique_kmer_nos)

