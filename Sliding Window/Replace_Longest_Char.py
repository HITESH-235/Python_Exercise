# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character. After performing at most k replacements, return the length of the longest substring which contains only one distinct character
# LEETCODE link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

def brute_force(s, k):
    res = 0

    for i in range(len(s)):
        count = {}
        max_count = 0

        for j in range(i, len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            max_count = max(max_count, count[s[j]])

            if (j-i+1) - max_count <= k:
                res = max(res, j-i+1)
    return res


def sliding_window(s, k):
    res = 0
    left = 0
    max_count = 0
    count = [0 for _ in range(26)]

    for right in range(len(s)):
        ind = ord(s[right]) - ord("A")
        count[ind] += 1
        max_count = max(max_count, count[ind])

        while right-left+1 - max_count > k:
            ind = ord(s[left]) - ord("A")
            count[ind] -= 1
            left += 1

        res = max(res, right-left+1)
    return res


s = "ABABBASHFGKJSHGJKDHGDKJFHGJDKFGHDGHDHGDHSDFDFDFFDFDFDFDFDFDFDFDFDFFHGHFGFHGJDFHKDSGHJKSFHJSDHFGJKSDFHSDF"
k = 31
from time import time

start = time()
print("\nBrute Force:", brute_force(s, k))
end = time()
print(f"{((end- start)*1000):.3f} milli-sec\n")

start = time()
print("Sliding Window:", sliding_window(s, k))
end= time()
print(f"{((end - start)*1000):.3f} milli-sec\n")