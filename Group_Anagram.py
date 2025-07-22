#GROUP ANAGRAM: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#LEETCODE link: https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

def group_anagram(lst):
    dct = defaultdict(list)
    for str in lst:
        char = [0]*26
        for x in str:
            char[ord(x)-ord("a")] += 1  #e.g. for word aabcc: [2,1,2,0,0,0,0,0..........26 elements]
        dct[tuple(char)].append(str)   #the words with the same key gets appended in an empty list (as value)
        #tuple is there because list are not allowed as keys
    return list(dct.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagram(strs))