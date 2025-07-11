# Given an integer, convert it to a Roman numeral
# LEETCODE link: https://leetcode.com/problems/integer-to-roman/description/

def intToRoman(num):
    # dataset for checking symbols and corresponding values:
    num_lst = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_lst = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    ans = ''                                    # empty string for storing answer
    for x in range(13):

        if num // num_lst[x] != 0:

            symbol = roman_lst[x]               # var to store largest suitable symbol
            count = num//num_lst[x]             # and its values
            ans += symbol * count
            num %= num_lst[x]

    return ans

print(intToRoman(2674))             # MMDCLXXIV
print(intToRoman(3888))             # MMMDCCCLXXXVIII
print(intToRoman(1299))             # MCCXCIX
print(intToRoman(984))              # CMLXXXIV