def process_list(mylist):

  # Modify each element in the list based on its parity and position.
  for i in range(len(mylist)):

    if mylist[i] % 2 == 0:
      
      mylist[i] /= 2  # Integer division for even numbers

    else:
      
      mylist[i] *= 2   # Multiplication for odd numbers

    if i % 7 == 0:
      
      mylist[i] += i   # Add the index if it's a multiple of 7

  # Return the maximum value in the modified list.
  return max(mylist)

my_list = [2, 3, 4, 4, 7, 7, 8, 9, 10, 1, 1]

max = process_list(my_list)

print(max)