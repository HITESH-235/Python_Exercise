def bucket_sort(lst):
    n = len(lst)
    sorted_lst = []

    bucket_s = [[] for useless_var in range(n)] #LIST COMPREHENSION
    # for i in range(n):
        # bucket_s.append([])

    for num in lst:
        rnge = int(num*n) #range for the class of numbers (just create of suitable width)
        bucket_s[rnge].append(num) 

    for bucket in bucket_s:
        bucket.sort() #sorts element inside each range
        # sorted_lst.append(bucket)
        sorted_lst.extend(bucket)

    return sorted_lst
    
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(bucket_sort(arr))
