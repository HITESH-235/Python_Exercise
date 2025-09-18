# Longest Palindromic Substring: return the largest palindromic (in sequence) substring from given string
# LEETCODE link: https://leetcode.com/problems/longest-palindromic-substring/description/

# Brute Force: O(n^3)
def longestPalindromicSubstring_BF(s):
    def isPalindromic(substring):
        return substring == substring[::-1]
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            is_palindromic = isPalindromic(substring) # return true or false
            if is_palindromic and len(longest)<(j-i+1):
                longest = substring
    return longest

# Optimised: O(n^2)
def longestPalindromicSubstring_Optimised(s): #TC:N**2; SC = N
    def expand(s,left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    # left and right have moved beyond correct palindrome
    # thus we need to slice from (left+1) --> (right-1)
    longest = ""
    n = len(s)
    for i in range(n):
        p_odd = expand(s,i,i)
        p_even = expand(s,i,i+1)
        if len(p_even) > len(longest):
            longest = p_even
        if len(p_odd) > len(longest):
            longest = p_odd
    return longest

s = "abababab"
s = "a"
print(longestPalindromicSubstring_BF(s))
print(longestPalindromicSubstring_Optimised(s))