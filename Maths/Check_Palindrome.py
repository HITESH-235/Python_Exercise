def check_palindrome(num):
    dup = num
    reverse = 0
    while dup>0:
        last = dup%10
        dup //= 10
        reverse *= 10
        reverse += last
    return (reverse == num)

num = 12234543221
print(check_palindrome(num))