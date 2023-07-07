def isValid(s):
    dicti = {"(": 1, ")": -1, "{": 2, "}": -2, "[": 3, "]": -3}
    reverse_dicti = {value: key for key, value in dicti.items()}
    nums = []
    for x in s:
        if dicti[x] > 0:
            nums.append(dicti[x])
        elif dicti[x] < 0:
            if not nums or reverse_dicti[-nums.pop()] != x:
                return False
    
                
    
    return nums == []
    
print("1: ()[]{} : ",isValid("()[]{}"))
print("2: ([)] : ",isValid("([)]"))
print("3: () : ",isValid("()"))
print("4: ((([][]{}{})))()[]{}[]() : ",isValid("((([][]{}{})))()[]{}[]()"))
print("5: ]]][[[ : ",isValid("]]][[["))
print("6: ] : ",isValid("]"))
print("7: {{{)))}} : ",isValid("{{{)))}}"))
print("8: [] : ",isValid("[]"))
print("9: {} : ",isValid("{}"))
print("10: (){}}{ : ",isValid("(){}}{"))
print("11: (]  : ", isValid("(]"))

