x = int(input("Please enter an integer - "))

sequence = []

print(x)

while x != 1 :

    sequence.append(x)

    if x % 2 == 0:

        x = x/2

    else :

        x = x * 3 + 1

sequence.append(1)

print(sequence)

print("All postive integers are known to be terminating to the 4 -> 2 -> 1 -> 4 sequence, hence no value of x exists for which this never happens.")