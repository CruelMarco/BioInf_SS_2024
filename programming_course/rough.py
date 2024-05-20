def g():
       x, n = 1
       while True:
           yield n
           n *= x
           x += 1

gen = g()
print([next(gen) for _ in range(10)])