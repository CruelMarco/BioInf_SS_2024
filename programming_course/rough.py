from collections import Counter

a = ["1" , "2" , "3" , "1" , "2" , "3"]

c = Counter(a)

dups = [i for i in c if c[i] > 1]

print(dups)