import math
x = 999
stroka = str(x)
lengthstr = len(stroka)
celoe = [int(simb) for simb in stroka]
centr = math.floor(lengthstr / 2)
if lengthstr == 1 and x > 0:
    print ("True")
else:
    lengthstr = lengthstr - 1

    for simbol in celoe[:centr]:
        s = simbol - celoe[lengthstr]
        lengthstr = lengthstr - 1
    if s == 0:
        print ("True")
    else: print ("False")
    
    
    



