def shift_or(text, pattern):

    pattern_length = len(pattern)

    pattern_mask = [0xFFFFFFFFFFFFFFFF] * 256

    R = ~1

    for i in range(pattern_length):

        pattern_mask[ord(pattern[i])] &= ~(1 << i)

    for i in range(len(text)):

        R |= pattern_mask[ord(text[i])]

        R <<= 1

        if R & (1 << pattern_length) == 0:

            return i - pattern_length + 1
        
    return -1


text = "ABABABCCACABAC"

pattern = "ABABC"

position = shift_or(text, pattern)

print(position)