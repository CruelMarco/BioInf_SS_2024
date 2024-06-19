def get_treasure(filename):
    # Step 1: Read the initial list from the file
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    
    n = len(numbers)
    
    # Step 2: Rearrange the list
    # We need a list of tuples (index, value) to keep track of the original positions
    indexed_numbers = list(enumerate(numbers))
    
    for i, value in enumerate(numbers):
        if value == 0:
            continue
        
        # Find the current index of the value
        current_index = next(index for index, (orig_i, val) in enumerate(indexed_numbers) if orig_i == i)
        
        # Remove the element from its current position
        element = indexed_numbers.pop(current_index)
        
        # Calculate the new index, wrapping around the list
        new_index = (current_index + value) % (n - 1)
        if new_index < 0:
            new_index += n - 1
        
        # Insert the element at its new position
        indexed_numbers.insert(new_index, element)
    
    # Reconstruct the rearranged list
    rearranged_list = [val for _, val in indexed_numbers]
    
    # Step 3: Compute the room number
    # Find the index of 0
    zero_index = rearranged_list.index(0)
    
    # Calculate the indices for the 1000th, 2000th, and 3000th numbers after 0
    index_1000 = (zero_index + 1000) % n
    index_2000 = (zero_index + 2000) % n
    index_3000 = (zero_index + 3000) % n
    
    # Sum the numbers at these positions
    room_number = rearranged_list[index_1000] + rearranged_list[index_2000] + rearranged_list[index_3000]
    
    return room_number

# Usage example (with the provided file):
filename = '/Users/shaique/Desktop/BioInf_IMP/BioInf_SS_2024/programming_course/assigment_codes/assignment_04/ass_04.2.txt'
print(get_treasure(filename))
