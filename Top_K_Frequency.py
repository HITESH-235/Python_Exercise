# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# LEETCODE link: https://leetcode.com/problems/top-k-frequent-elements/description/

def top_k( lst, k ):
    count = {}
    n = len(lst) + 1

    buckets = [[] for _ in range(n)]

    for num in lst:
        count[num] = 1+count.get(num,0) #keys:items in lst, values:their frequency 

    for n,c in count.items():
        buckets[c].append(n)  #bucket stores the number accord to freq. (low to high) 

    sorted_lst  = []
    for ind in range(len(buckets)-1,0,-1):
        sorted_lst.extend(buckets[ind])
        if len(sorted_lst) >= k:
            return sorted_lst[0:k]
            
        # for num in buckets[ind]:
        #     sorted_lst.append(num)
        #     if len(sorted_lst) == k:
        #         return sorted_lst

    return "value of k exceeded length"
    
print(top_k([1,1,1,1,1,1,2,3,4,4,4,4,6,7,8,8,8,8,9,5,5],3))
