import itertools as it

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

print(is_vampire(125460))



def vampire_generator():
    
    n = 1260 
    
    while True:
        if is_vampire(n):
            yield n
        n += 1 

# Example usage
if __name__ == "__main__":
    print("First 10 vampire numbers:")
    vampire_gen = vampire_generator()
    for _ in range(10):
        print(next(vampire_gen))





