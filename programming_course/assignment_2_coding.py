#Contributed by Shaique - moso00002 and Sandhya - saba00012

#Algorithm Referred for understanding from https://iq.opengenus.org/shift-or-algorithm-for-string-matching/


def shift_or(text, pattern):
    pattern_length = len(pattern)
    pattern_mask = [0xFFFFFFFFFFFFFFFF] * 256
    R = ~1

    if pattern_length == 0:
        return -1  # If no pattern has been given.
    if pattern_length > 63:
        print("Pattern is too long!")
        return -1

    for i in range(pattern_length):
        pattern_mask[ord(pattern[i])] &= ~(1 << i)

    for i in range(len(text)):
        R |= pattern_mask[ord(text[i])]
        R <<= 1
        if R & (1 << pattern_length) == 0:
            return i - pattern_length + 1
    return -1

def find_pattern(text, pattern):
    position = shift_or(text, pattern)
    if position == -1:
        print("\nNo Match")
    else:
        print("\nPattern found at position:", position)

if __name__ == "__main__":
    text = "opengenus"
    pattern = "genus"
    find_pattern(text, pattern)