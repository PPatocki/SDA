
# sortowanie bombelkowe

l=[8, 7, 6, 5, 4, 3, 2, 1]

def bubble_sort(l):
    n = len(l)
    while n>1:
        for i in range(n-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
        n-=1
    return l

print(bubble_sort(l))
