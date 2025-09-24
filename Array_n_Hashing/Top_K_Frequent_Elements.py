# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# LEETCODE link: https://leetcode.com/problems/top-k-frequent-elements/description/


def top_k_frequent(lst, k):
    frequency_map = {}
    n = len(lst)
    if n <= k:
        return list(set(lst))
    # if n <= k: then we can only return every unique num in list

    buckets = [[] for _ in range(n+1)] # makes 0,1,2,3....n indices
    # because the maximum frequency can be n in a n indexed list

    for num in lst:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    for num, freq in frequency_map.items():
        buckets[freq].append(num)
    # e.g. num with 3 frequency goes to 3rd index
    # num with n frequency(max possible) goes to nth index
    # hence their could be multiple unique nums in same bucket

    results = []
    for freq in range(n, -1, -1):
        results.extend(buckets[freq]) # most frequent elements will be at back of buckets
        # suppose nth bucket is empty, then results will remain unchanged

        if len(results) >= k: # we stop when k or more than k uniques are found
            return results[:k] # catching only top k's, as more than k may have entered results

    return results[:k] # just in case loop ended without returning

print(top_k_frequent([1,1,1,1,1,4,4,4,4,8,8,8,5,6,7,7,9],25)) # returns [1,4,8]