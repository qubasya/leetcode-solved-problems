def is_palindrome(x):
    
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverse_num = 0
    original_num = x

    while x > 0:
        last_digit = x % 10
        reverse_num = reverse_num * 10 + last_digit
        x //= 10

    return original_num == reverse_num


print(is_palindrome(989)) 

