####
###Contributed by Mohammad Shaique Solanki -  moso00002 and Sandhya Badiger - saba00012



def hosrpool_preprocessing(pattern, l): ##Preprocessing function taken from slides
    table = {}
    m = len(pattern)
    for i in range(m - l):
        table[pattern[i:i+l]] = m - l - i
    return table

def horspool_search(text, pattern, l): ##Horspool search function taken from slides and edited
    n = len(text)
    m = len(pattern)
    if n < m:
        return [], 0, 0

    pos = []
    comps = 0
    shifts = 0

    skip_dict = hosrpool_preprocessing(pattern, l)
    i = 0

    while i <= n - m:
        j = m - l
        while j >= 0 and pattern[j:j+l] == text[i + j:i + j + l]:
            j -= l
            comps += 1
        if j == -l:
            pos.append(i)
        shifts += 1
        i += skip_dict.get(text[i + m - l:i + m], m - l)

    return pos, comps, shifts

text = "ABAABABABABBABABAABBBABACABBBABABBABABAABABCBABC"
pattern= "ABABBABABA"

for l in range(1, 4):
    matching_positions, comparison_count, shift_count = horspool_search(text, pattern, l)
    print(f"Pattern length l = {l}")
    print("Matching positions:", matching_positions)
    print("Comparison count:", comparison_count)
    print("Shift count:", shift_count)
    print()
