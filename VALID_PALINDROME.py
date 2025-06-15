#VALID PALINDROME: Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.
#LEETCODE link: https://leetcode.com/problems/valid-palindrome/description/

def filter(str):
    for a in str:
        if a.isalnum() == False:
            str = str.replace(a,"")
    return str

def method1(str):
    left, right = 0, len(str)-1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

def method2(str):
    if str == str[::-1]: #checks for reverse
        return True
    return False

str = "123a%$^$bg5*&*----gba321"
print(method8(filter(str)))
print(method9(filter(str)))
