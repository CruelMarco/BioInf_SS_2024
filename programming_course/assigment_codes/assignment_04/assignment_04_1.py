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
