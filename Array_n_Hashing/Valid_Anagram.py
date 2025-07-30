#VALID_ANAGRAM: Given two strings s and t, return true if t is an anagram of s, and false otherwise. 
#LEETCODE_link: https://leetcode.com/problems/valid-anagram/description/

#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def method_1(a,b):
    t = list(a)
    u = list(b)
    t.sort()
    u.sort()
    if (t == u):
        return "True"
    else:
        return "False"

from collections import Counter
#counter is used to store repititions of character of a string or list into a dictionary:
def method_2(a,b):
    return Counter(a) == Counter(b)

#dictionary method (manually)
def method_3(a,b):
    if len(a) != len(b):    #For cases where string are unequal, directly give false
        return False
    count = {}
    for char in a:
        count[char] = count.get(char,0)+1 #get doesnt add key if DNE but returns value

    for char in b:
        if char not in count:
            return False
        count[char] -= 1 #decrese count each time same char found in t
        if count[char] < 0:#if count goes -ve means that t had more of that char than s
            return False
    return True

s = "anagram"
t = "naagram"
print(method_1(s,t))
print(method_2(s,t))
print(method_3(s,t))
