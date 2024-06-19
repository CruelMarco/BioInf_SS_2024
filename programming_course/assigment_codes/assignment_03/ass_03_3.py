def solve(n, operations):
    calc_elemets = operations.split(" ")

    operations_list = ["add" , "mul" , "div" , "mod"]

    operation_seq = calc_elemets[::2]

    num_seq = calc_elemets[1::2]

    if len(operation_seq) != len(num_seq):

        return -1

    else:

        for i in range (len(operation_seq)):

            match operation_seq[i]:

                case "add":

                    n = n + int(num_seq[i])
                
                case "mul":

                    n = n * int(num_seq[i])

                case "div":

                    n = n / int(num_seq[i])

                case "mod":

                    n = n % int(num_seq[i])

        return n
        

print(solve(10, "add 6 mul 2 div 4 mod 5 mul 3"))

    
 

