# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# LEETCODE link: https://leetcode.com/problems/top-k-frequent-elements/description/


def top_k_frequent(lst, k):
    frequency_map = {}
    n = len(lst)
    buckets = [[] for _ in range(n+1)]

    for num in lst:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    for value, freq in frequency_map.items():
        buckets[freq].append(value)     

    results = []
    for freq in range(n-1, -1, -1):
        results.extend(buckets[freq])
        if len(results) >= k:
            return results[:k]
    return "K exceeds length of given array!"

print(top_k_frequent([1,1,1,1,1,1,2,3,4,4,4,4,6,7,8,8,8,8,9,5,5],3)) # returns [1,4,8]