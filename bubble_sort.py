def bubble_sort(s):
    lst = list(s)
    for i in range(len(s),0,-1):
        for j in range(0,i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    s = str(lst)
    return s

s = "randomstring"
print(bubble_sort(s))
