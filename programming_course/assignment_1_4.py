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

def decode_kmer(code, k):
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

integer_code = kmer_code('ACTG')

decoded = decode_kmer(30, 4)

print(integer_code)

print(decoded)