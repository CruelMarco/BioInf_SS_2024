def hamming_distance(filename):

    f = open(filename, 'r')

    lines = f.readlines()

    lines = [i.strip() for i in lines ]

    valid_chars = set("ACGTU")

    for seq in lines:

        for char in seq.upper():

            if char not in valid_chars:

                return (-1,-1)
    if not all(len(seq) == len(lines[0]) for seq in lines):

        return (-1, -1)

    line = [i.upper().replace("U" , "T") for i in lines]

    combinations = []

    for i in range(len(line)):

        for j in range(i+1, len(line)):

            combinations.append([line[i] , line[j]])

    def hamming_dist(str1, str2): 
        i = 0
        count = 0

        for i in range(len(str1)):

            if(str1[i] != str2[i]):

                count = count + 1
            i = i + 1
        
        return count

    distance = []

    for k in combinations:

        str1 , str2 = k[0], k[1]

        if len(str1) != len(str2):

            return(-1,-1)

        else:

            dist = hamming_dist(str1, str2)

            distance.append(dist)

    min_distance = min(distance)

    max_distance = max(distance)

    return (min_distance , max_distance)

print(hamming_distance("ass_02.2.txt"))





