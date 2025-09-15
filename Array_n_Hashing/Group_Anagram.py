# GROUP ANAGRAM: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# LEETCODE link: https://leetcode.com/problems/group-anagrams/description/

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


# ______________________________________________________Procedure Explained:________________________________________________

# 1.Create function which takes given list of strings as input

# 2.Create a default dictionary which takes empty list as values (keys are going to be tuple of char)
#   Start loop through the string
#   Inside list create a char_list of 26 0s (to be updated further) (created everytime for new string)

# 3.loop through the curr string
#   increase the value of the curr alphabet index by 1 in char_list
#   get index using ascii values: ord(curr_alphabet) - ord(a)
#   char_list is actually storing the frequency of alphabets, which is unique for an anagram

# 4.come out of loop in curr string,
#   convert char_list to tuple, store the char_tuple in dictionary as key (because list cant be keys)
#   for this char_tuple, the value is initially an empty list, update it with the curr_string
#   everytime a string, anagram to it, comes, will append in the the same (value)list of its corresp. (key)char_tuple

# 5.Hence return the only the values(lists) of this dictionary, such that they are in a parent list

# __________________________________________________________________________________________________________________________