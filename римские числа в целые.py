def romanToInt(s):
    puk = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    resultat = 0
    prev_val = 0

    for simb in reversed(s):
        curr_val = puk[simb]
        if curr_val >= prev_val:
            resultat += curr_val
        else:
            resultat -= curr_val
        prev_val = curr_val

    return resultat

print(romanToInt("MCMXCIV"))


