def preprocess_pattern(pattern):
    table = {}
    m = len(pattern)
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table

def horspool(text, pattern):
    n = len(text)
    m = len(pattern)
    if n < m:
        return []

    positions = []
    skip_table = preprocess_pattern(pattern)
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == -1:
            positions.append(i)
        i += skip_table.get(text[i + m - 1], m)

    return positions

T = "ABAABABABABBABABAABBBABACABBBABABBABABAABABCBABC"
P = "ABABBABABA"

matching_positions = horspool(T, P)
print("Matching positions:", matching_positions)
