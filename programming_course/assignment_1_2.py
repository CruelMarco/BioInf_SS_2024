def dna_changer(str):

    changed_dna = ""

    for i in str[::-1]:

        if i == "A":

            changed_dna = changed_dna + "T"

        elif i == "T":

            changed_dna = changed_dna + "A"

        elif i == "G":

           changed_dna = changed_dna + "C"

        else:

            changed_dna = changed_dna + "G"

    return(changed_dna)

str_og = "ACGATCGATCG"

change = dna_changer(str_og)

print(change)

        
