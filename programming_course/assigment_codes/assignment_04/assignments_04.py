import numpy as np

class CountingBloomFilter:
    def __init__(self, m, k, hash):
        self.m = m
        self.k = k
        self.hash = hash
        self.filter = np.zeros(m, dtype=np.uint8)
        
    def __hash__(self, x, i):
        return (x * self.hash[i]) % self.m

    def insert(self, x):
        for i in range(self.k):
            index = self.__hash__(x, i)
            self.filter[index] += 1

    def delete(self, x):
        for i in range(self.k):
            index = self.__hash__(x, i)
            if self.filter[index] > 0:
                self.filter[index] -= 1

    def contains(self, x):
        for i in range(self.k):
            index = self.__hash__(x, i)
            if self.filter[index] == 0:
                return False
        return True

    def count(self, x):
        return min(self.filter[self.__hash__(x, i)] for i in range(self.k))


    def __hash__(self, x, i):

        return (x * self.hash[i]) % self.m
    
        pass


def get_treasure(filename):
    
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    
    n = len(numbers)
    
    indexed_nums = list(enumerate(numbers))
    
    for i, value in enumerate(numbers):
        if value == 0:
            continue
        
        curr_ind = next(index for index, (i_org, val) in enumerate(indexed_nums) if i_org == i)
        
        element = indexed_nums.pop(curr_ind)
        
        new_index = (curr_ind + value) % (n - 1)
        if new_index < 0:
            new_index += n - 1

        indexed_nums.insert(new_index, element)
    

    rearranged_list = [val for _, val in indexed_nums]
    

    zero_index = rearranged_list.index(0)
    
    index_1000 = (zero_index + 1000) % n
    index_2000 = (zero_index + 2000) % n
    index_3000 = (zero_index + 3000) % n
    
    # Sum the numbers at these positions
    room_number = rearranged_list[index_1000] + rearranged_list[index_2000] + rearranged_list[index_3000]
    
    return room_number
    
    
    pass
    



def quantile_normalize(matrix):

    sorted_matrix = np.sort(matrix, axis=0)
    
    rank_means = np.mean(sorted_matrix, axis=1)
    
    ranks = np.argsort(np.argsort(matrix, axis=0), axis=0)
    
    normalized_matrix = np.zeros(matrix.shape)
    for col in range(matrix.shape[1]):
        normalized_matrix[:, col] = rank_means[ranks[:, col]]
    
    return normalized_matrix
    pass