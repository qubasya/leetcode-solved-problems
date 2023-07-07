def romanToInt(num):
    puk = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}#просто - , 5000: "G", 10000: "J"}
    resultat = ''
    i = 1
    while num > 0:
        test = num % 10
        if test != 0:
            last_digit = num % 10 * i
            pampam = last_digit
            if test == 4 or test == 9:
                for x, y in puk.items():
                    z = last_digit + x 
                    if z in puk:
                        resultat = puk[x] + puk[z] + resultat 
            else:
                tuk = num
                prev_num = 0
                result = ''
                for reverslist in reversed(puk):            
                    if last_digit >= reverslist:
                        pampam = last_digit // reverslist
                        last_digit = last_digit - reverslist * pampam
                        result = result + puk[reverslist] * pampam 
                resultat = result + resultat
        i = i * 10
        num //= 10
    return resultat
print(romanToInt(1107))


